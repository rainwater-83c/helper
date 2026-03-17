import discord
from discord.ext import commands
import os
import config
import asyncio
import logging
import sys

if not os.path.exists("logs"):
    os.makedirs("logs")
log_format = logging.Formatter(
    "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(log_format)
logfile_handler = logging.FileHandler("logs/bot.log", mode="w")
logfile_handler.setFormatter(log_format)
log = logging.getLogger("discord")
log.setLevel(logging.INFO)
log.addHandler(stdout_handler)
log.addHandler(logfile_handler)

intents = discord.Intents.all()
intents.typing = False

bot = commands.Bot(
    command_prefix=None,
    description=config.short_desc,
    owner_ids=set(config.managers),
    intents=intents,
    enable_debug_events=True,  # for raw events (e.g. super reactions handler)
)

bot.help_command = None
bot.log = log
bot.config = config
bot.version = config.version

@bot.event
async def on_ready():
    log.info(f"\nLogged in as: {bot.user.name} - {bot.user.id}")
    await bot.tree.sync()
# context menu commands cannot be placed in cogs




async def main():
    async with bot:
        for cog in [
            "cogs." + f[:-3]
            for f in os.listdir("cogs/")
            if os.path.isfile("cogs/" + f) and f[-3:] == ".py"
        ]:
            try:
                await bot.load_extension(cog)
            except:
                log.exception(f"Failed to load cog {cog}.")
        await bot.start(config.token)

if __name__ == "__main__":
    asyncio.run(main())