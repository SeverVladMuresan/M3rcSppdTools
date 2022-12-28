import datetime

from HUMAN_FRIENDLY_HELPER import human_friendlyfy_card_requests


class BotMessageService:
    CARD_REQUEST_NOTIFIER_MENTION = '@CardRequestNotifier'
    CARD_REQUEST_NOTIFIER_THRESHOLD = datetime.timedelta(hours=1, minutes=10)

    @staticmethod
    def build_message(unfilled_card_requests_about_to_expire):

        BotMessageService.__validate_unfilled_card_requests_about_to_expire(unfilled_card_requests_about_to_expire)

        if BotMessageService.__is_empty(unfilled_card_requests_about_to_expire):
            return BotMessageService.__every_card_requests_filled_message(unfilled_card_requests_about_to_expire)

        BotMessageService.__human_friendlyfy_card_requests_dictionary(unfilled_card_requests_about_to_expire)

        messages_for_each_timedelta = []
        for expiry_time_delta, card_requests in unfilled_card_requests_about_to_expire.items():
            messages_for_each_timedelta.append(BotMessageService.
                                               __build_message_for_delta_time(expiry_time_delta, card_requests))

        return '\n\n'.join(messages_for_each_timedelta)

    @staticmethod
    def __build_message_for_delta_time(expiry_time_delta, card_requests):
        if not card_requests:
            return ''

        discord_mention_if_needed_blank_if_not = BotMessageService.CARD_REQUEST_NOTIFIER_MENTION \
            if expiry_time_delta < BotMessageService.CARD_REQUEST_NOTIFIER_THRESHOLD else ''
        expiry_time_delta_formatted = str(expiry_time_delta)
        msg = "{0}The following card requests will expire in **less than [{1}]**:" \
            .format(discord_mention_if_needed_blank_if_not, expiry_time_delta_formatted)

        card_request_messages = [msg]
        for cr in card_requests:
            card_request_messages.append("{0} requested by {1} with {2}/{3} copies donated"
                                         .format(cr['card_name'], cr['profile_name'], cr['copies'], cr['max_copies']))

        return '\n'.join(card_request_messages)

    @staticmethod
    def __human_friendlyfy_card_requests_dictionary(unfilled_card_requests_about_to_expire):
        for expiry_time_delta, card_requests in unfilled_card_requests_about_to_expire.items():
            human_friendlyfy_card_requests(card_requests)

    @staticmethod
    def __every_card_requests_filled_message(unfilled_card_requests_about_to_expire):

        max_time_delta = max(list(unfilled_card_requests_about_to_expire.keys()))

        max_time_delta_formatted = str(max_time_delta)
        return "There are no unfilled card requests that are about to expire " \
               "in **[" + max_time_delta_formatted + "]**\n"

    @staticmethod
    def __is_empty(unfilled_card_requests_about_to_expire):
        for key, card_requests in unfilled_card_requests_about_to_expire.items():
            if card_requests:
                return False

        return True

    @staticmethod
    def __validate_unfilled_card_requests_about_to_expire(unfilled_card_requests_about_to_expire):
        if not unfilled_card_requests_about_to_expire:
            raise Exception("unfilled_card_requests_about_to_expire is empty")
