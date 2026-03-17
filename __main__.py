import discord
from discord.ext import commands
import os
import config

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
bot.config = config
bot.version = config.version


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