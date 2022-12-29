import discord


class DiscordRoleService:
    CARD_REQUEST_NOTIFIER_MENTION_NAME = 'CardRequestNotifierAAA'
    CARD_REQUEST_NOTIFIER_ROLE = None

    @staticmethod
    def get_card_request_notifier_role(ctx):
        DiscordRoleService.__init_card_request_role(ctx)
        return DiscordRoleService.CARD_REQUEST_NOTIFIER_ROLE

    @staticmethod
    def get_card_request_notifier_role_mention(ctx):
        DiscordRoleService.__init_card_request_role(ctx)
        return DiscordRoleService.CARD_REQUEST_NOTIFIER_ROLE.mention if DiscordRoleService.CARD_REQUEST_NOTIFIER_ROLE \
            else ""

    @staticmethod
    def __init_card_request_role(ctx):
        if not DiscordRoleService.CARD_REQUEST_NOTIFIER_ROLE:
            DiscordRoleService.CARD_REQUEST_NOTIFIER_ROLE = \
                discord.utils.get(ctx.guild.roles, name=DiscordRoleService.CARD_REQUEST_NOTIFIER_MENTION_NAME)
