import asyncio
import os

import discord
from discord.ext import commands

from pool_price_info import get_pool_btc_tick

bot = commands.Bot(command_prefix=".")
token = os.getenv("BOT_TOKEN")
guild_id = int(os.getenv("GUILD_ID"))


async def send_update():
    nickname = get_pool_btc_tick()
    activity_status = "UniV3 pool"
    await bot.get_guild(guild_id).me.edit(nick=nickname)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=activity_status
        )
    )
    await asyncio.sleep(60)


@bot.event
async def on_ready():
    """
    When discord client is ready
    """
    while True:
        await send_update()


bot.run(token)
