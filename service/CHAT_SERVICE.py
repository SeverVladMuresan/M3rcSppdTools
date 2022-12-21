import SPPD_API

# -----------------------------------------------------------
#
#This file only contains scraps of code that can be used for chat - which also contains card donations
#Such code is currently unused
#
# -----------------------------------------------------------


# class ChatService:



# Get the ingame_team_id from [already grabbed] |||||          "id": 141350,
# print(getTeamID('M3RCENARIES'))
# Get the ubimobi_access_token from getUbiMobiAccessToken  ||| 'ubimobi_access_token': 'Ow5QqAOXOD2TeiFPVmA1F1m7plAu3pUSW0ImBxkpanjpGZeBmPD1R09glJKp9Fi6'}
# print(SPPD_API.getUbiMobiAccessToken(PROFILE_ID))


# def get_ubimobi_access_token(profile_id):
#     parsed_response = SPPD_API.getUbiMobiAccessToken(profile_id)
#     return parsed_response['device']['ubimobi_access_token']
#
# print (SPPD_API.getUbiMobiAccessToken("6a7206d8-e9e0-4a2b-80ec-acf59407f226"))
#
# def get_latest_game_session(parsed_team_init_response):
#     game_sessions = parsed_team_init_response['chat']['game_sessions']
#     latest_game_session = game_sessions[0]
#     for game_session in game_sessions[1:]:
#         if game_session['expires'] >= latest_game_session['expires']:
#             latest_game_session = game_session
#
#     return latest_game_session
#
# parsed_team_init_response = SPPD_API.getTeamInit()
# latest_game_session = get_latest_game_session(parsed_team_init_response)
#
#
# # Get the game_session_id from getTeamInit ||||               'id': '26LDLyj5dW1HZM3qbMXe68UK0VvP0WGF'
# # Get the game_session_id from getTeamInit ||||               'cluster': 'gamesrv02-mob.ubi.com'
# # Get the game_session_id from getTeamInit ||||               'bucket': 'clan_chat_141350',
#
# # print(SPPD_API.getTeamInit());
# cluster = latest_game_session['cluster']
# bucket = parsed_team_init_response['chat']['bucket']
# ubimobi_access_token = get_ubimobi_access_token('6a7206d8-e9e0-4a2b-80ec-acf59407f226')
#
# game_session_id = latest_game_session['id']
#
# # print(cluster)
# # print(bucket)
# # print(ubimobi_access_token)
# # print(game_session_id)
#
# teamChat = SPPD_API.getTeamChat(cluster, bucket, ubimobi_access_token, game_session_id)
# print(teamChat)
