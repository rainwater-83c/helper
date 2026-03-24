import discord
from discord.ext import commands
import os
import config
from discord import app_commands
import asyncio
from io import BytesIO
import requests
import logging
import sys
from helpers.datafiles import make_userfile, get_userfile, set_userfile

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
    command_prefix="hlp ",
    description=config.short_desc,
    owner_ids=set(config.managers),
    intents=intents,
    enable_debug_events=True,  # for raw events (e.g. super reactions handler)
)

bot.help_command = None
bot.log = log
bot.config = config
bot.version = config.version

@bot.command()
@commands.is_owner()

async def sync(ctx: commands.Context):
    await bot.tree.sync()
    await ctx.send("Commands synced globally!")
    log.info("*")
    for command in bot.tree.walk_commands():
        log.info(f"* {command.name}")
    log.info("*")

@bot.command()
@commands.is_owner()
async def syncguild(ctx: commands.Context):
    
    guild = discord.Object(id=1377274564282679457)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    await ctx.send("Commands synced!")
    log.info("*")
    for command in bot.tree.walk_commands(guild=guild):
        log.info(f"* {command.name}")
    log.info("*")

@bot.event
async def on_ready():
    log.info(f"\nLogged in as: {bot.user.name} - {bot.user.id}")


# context menu commands cannot be placed in cogs
@app_commands.allowed_installs(users=True, guilds=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.context_menu(name="petpet")
async def petpet(interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('pet', 0) + 1
            userfile['pet'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            file = discord.File(BytesIO(requests.get(f'https://tt7homa.eu.pythonanywhere.com/petpet.gif?image={user.avatar.url}').content), filename=f'{user.id}_petpet.gif')
            await interaction.response.send_message(user.mention, file=file)
            await interaction.followup.send(f"-# {user.name} has been pet {count} times.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")


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
