# https://discord.com/api/oauth2/authorize?client_id=1054510034387738655&permissions=274877906944&scope=bot
#
#
#

import os

import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

intents=discord.Intents.default()
# intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='start')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    i=0
    while True:
        response = brooklyn_99_quotes[i % len(brooklyn_99_quotes)]
        i = i + 1
        time.sleep(3)
        await ctx.send(response)


# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

bot.run(TOKEN)

