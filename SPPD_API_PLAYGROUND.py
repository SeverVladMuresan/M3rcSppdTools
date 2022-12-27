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


team_id = SPPD_API.getTeamID('M3RCENARIES')
print(team_id)

parsed_team_init_response = SPPD_API.getTeamInit()
print(parsed_team_init_response)

user_p = SPPD_API.getUserName('6a7206d8-e9e0-4a2b-80ec-acf59407f226')
user_r = SPPD_API.getUserName('4da3555f-8b8d-4803-b624-47c2c018fefa')

print(user_p)
print(user_r)

user_details_p = SPPD_API.getUserDetails('6a7206d8-e9e0-4a2b-80ec-acf59407f226')
user_details_r = SPPD_API.getUserDetails('6a7206d8-e9e0-4a2b-80ec-acf59407f226')

print(user_details_p)
print(user_details_r)


card_request_service = CardRequestService()

TIME_DELTAS = []
for i in [2, 1]:
    expiry_time_delta = datetime.timedelta(hours=i)
    TIME_DELTAS.append(expiry_time_delta)

unfilled_card_requests_about_to_expire = card_request_service.get_unfilled_card_requests_about_to_expire(TIME_DELTAS)

print("\n")
print("All card requests:")
print(card_request_service.card_requests)
print("Unfilled card requests:")
print(card_request_service.unfilled_card_requests)
print("Human friendly unfilled card requests:")
human_friendlyfy_card_requests(card_request_service.unfilled_card_requests)
print(card_request_service.unfilled_card_requests)

print("\n")
print("Card requests about to expire:")
for expiry_time_delta, card_requests in unfilled_card_requests_about_to_expire.items():
    print(expiry_time_delta)
    print(card_requests)
