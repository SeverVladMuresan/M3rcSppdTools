import datetime
import json

import SPPD_API


class CardRequestService:
    unfilled_card_requests = None

    # @staticmethod
    def __init__(self):
        self.unfilled_card_requests = CardRequestService.__get_unfilled_card_requests()

    @staticmethod
    def __get_card_requests():
        card_requests_response = SPPD_API.getCardRequests()
        parsed_response = json.loads(card_requests_response)
        card_requests = parsed_response['requests']
        return card_requests

    @staticmethod
    def __get_unfilled_card_requests():
        filtered = filter(lambda request: request['max_copies'] > request['copies'],
                          CardRequestService.__get_card_requests())
        return list(filtered)

    def get_unfilled_card_requests_about_to_expire(self, expiry_time_delta):
        now_datetime = datetime.datetime.now()
        unfilled_card_requests_about_to_expire = []

        for cr in self.unfilled_card_requests:
            cr_valid_until_datetime = datetime.datetime.fromtimestamp(cr['valid_until'])
            if now_datetime + expiry_time_delta > cr_valid_until_datetime:
                unfilled_card_requests_about_to_expire.append(cr)

        return unfilled_card_requests_about_to_expire

    def get_expired_card_requests(self, expiry_time_delta):

        expiry_time_interval_start = datetime.datetime.now() - expiry_time_delta
        expiry_time_interval_end = datetime.datetime.now()
        expired_card_requests = []

        for cr in self.unfilled_card_requests:
            cr_valid_until_datetime = datetime.datetime.fromtimestamp(cr['valid_until'])
            if (expiry_time_interval_start < cr_valid_until_datetime <= expiry_time_interval_end) \
                    and (cr['max_copies'] != cr['copies']):
                expired_card_requests.append(cr)

        return expired_card_requests
