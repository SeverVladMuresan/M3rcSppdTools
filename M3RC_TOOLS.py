import asyncio
import datetime
import os
import SPPD_API
from service.BOT_MESSAGE_SERVICE import BotMessageService
from service.CARD_REQUEST_SERVICE import CardRequestService
from service.DISCORD_ROLE_SERVICE import DiscordRoleService
from service.SCHEDULING_SERVICE import SchedulingService
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv


bot_started: bool = False

TIME_DELTAS = []
for i in [2, 1]:
    expiry_time_delta = datetime.timedelta(hours=i)
    TIME_DELTAS.append(expiry_time_delta)


async def display_unfilled_requests(ctx):
    card_request_service = CardRequestService()
    unfilled_card_requests_about_to_expire = card_request_service.get_unfilled_card_requests_about_to_expire(
        TIME_DELTAS)
    card_request_notifier_role_mention = DiscordRoleService.get_card_request_notifier_role_mention(ctx)
    await ctx.send(BotMessageService.build_message(unfilled_card_requests_about_to_expire,
                                                   card_request_notifier_role_mention))


@tasks.loop(minutes=30)
async def bot_action(ctx):
    await display_unfilled_requests(ctx)


@bot_action.before_loop
async def before_bot_action():
    future = SchedulingService.get_next_even_half_hour()
    await asyncio.sleep((future - datetime.datetime.now()).seconds)

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
USERNAME = os.getenv('GOOGLE_PLAY_USERNAME')
PASSWORD = os.getenv('GOOGLE_PLAY_PASSWORD')

SPPD_API.setUsernamePassword(USERNAME, PASSWORD)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='start')
async def start_bot(ctx):
    global bot_started
    bot_started = True
    await ctx.send("Bot started")
    bot_action.start(ctx)


@bot.command(name='display')
async def display(ctx):
    await display_unfilled_requests(ctx)


@bot.command(name='status')
async def bot_status(ctx):
    if bot_started:
        get_next_even_half_hour = SchedulingService.get_next_even_half_hour()
        next_update_time_delta = get_next_even_half_hour - datetime.datetime.now()
        get_next_even_half_hour_formatted = str(next_update_time_delta).split(".")[0]
        await ctx.send(str.format("Bot started\n"
                                  "The next update is scheduled in **[{0}]**", get_next_even_half_hour_formatted))
    else:
        await ctx.send("The bot is not started yet. To start it, type **!start** in the thread")
    await ctx.send("The mention that whill be used for card requests is: "
                   + str(DiscordRoleService.get_card_request_notifier_role(ctx)))


bot.run(DISCORD_TOKEN)

