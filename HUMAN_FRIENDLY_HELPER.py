import datetime

import SPPD_API
from service.CARD_NAME_SERVICE import CardNames


def human_friendlyfy_card_requests(card_requests):
    now_datetime = datetime.datetime.now()
    for cr in card_requests:
        cr['valid_until_human_friendly'] = get_human_friendly_date(cr['valid_until'])
        cr['created_human_friendly'] = get_human_friendly_date(cr['created'])
        cr['card_name'] = get_human_friendly_card_name(cr['card_id'])
        cr['profile_name'] = get_human_friendly_username(cr['profile_id'])
        cr_valid_until_datetime = datetime.datetime.fromtimestamp(cr['valid_until'])
        expiry = cr_valid_until_datetime - now_datetime
        cr['expiry'] = expiry.__str__()


def get_human_friendly_username(profile_id):
    parsed_response = SPPD_API.getUserName(profile_id)
    return parsed_response['profiles'][0]['nameOnPlatform']


def get_human_friendly_card_name(card_id):
    return CardNames.get_card_name(card_id)


def get_human_friendly_date(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).isoformat().replace('T', ' ')
