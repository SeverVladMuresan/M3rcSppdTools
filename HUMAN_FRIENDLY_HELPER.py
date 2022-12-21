import datetime

import SPPD_API
from service.CARD_NAME_SERVICE import CardNames


def human_friendlyfy_card_requests(card_requests):
    for r in card_requests:
        r['valid_until_human_friendly'] = get_human_friendly_date(r['valid_until'])
        r['created_human_friendly'] = get_human_friendly_date(r['created'])
        r['card_name'] = get_human_friendly_card_name(r['card_id'])
        r['profile_name'] = get_human_friendly_username(r['profile_id'])
    return card_requests


def get_human_friendly_username(profile_id):
    parsed_response = SPPD_API.getUserName(profile_id);
    return parsed_response['profiles'][0]['nameOnPlatform']


def get_human_friendly_card_name(card_id):
    return CardNames.get_card_name(card_id)


def get_human_friendly_date(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).isoformat().replace('T', ' ')
