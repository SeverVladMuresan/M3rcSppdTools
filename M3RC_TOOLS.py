import datetime
import os

import SPPD_API
from HUMAN_FRIENDLY_HELPER import human_friendlyfy_card_requests
from service.CARD_REQUEST_SERVICE import CardRequestService
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('GOOGLE_PLAY_USERNAME')
PASSWORD = os.getenv('GOOGLE_PLAY_PASSWORD')


SPPD_API.setUsernamePassword(USERNAME, PASSWORD)

test_time_delta = datetime.timedelta(hours=1)
card_request_service = CardRequestService()

print(human_friendlyfy_card_requests(card_request_service.card_requests))

unfilled_card_requests_about_to_expire = card_request_service.get_unfilled_card_requests_about_to_expire(test_time_delta)
print(human_friendlyfy_card_requests(unfilled_card_requests_about_to_expire))

