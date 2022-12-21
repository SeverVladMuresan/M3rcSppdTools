import datetime
import json

import SPPD_API


class CardRequestService:
    card_requests = None
    unfilled_card_requests = None

    def __init__(self):
        self.card_requests = CardRequestService.__get_card_requests()
        self.unfilled_card_requests = self.__get_unfilled_card_requests()

    @staticmethod
    def __get_card_requests():
        card_requests_response = SPPD_API.getCardRequests()
        parsed_response = json.loads(card_requests_response)
        card_requests = parsed_response['requests']
        return card_requests

    def __get_unfilled_card_requests(self):
        filtered = filter(lambda request: request['max_copies'] > request['copies'],
                          self.card_requests)
        return list(filtered)

    def get_unfilled_card_requests_about_to_expire(self, expiry_time_delta):
        now_datetime = datetime.datetime.now()
        unfilled_card_requests_about_to_expire = []

        for cr in self.unfilled_card_requests:
            cr_valid_until_datetime = datetime.datetime.fromtimestamp(cr['valid_until'])
            if now_datetime + expiry_time_delta > cr_valid_until_datetime:
                unfilled_card_requests_about_to_expire.append(cr)

        return unfilled_card_requests_about_to_expire

    #Expired card requests are not sent via the SPPD Api
    def get_expired_card_requests(self, expiry_time_delta):
        raise NotImplementedError("Not implemented yet")

