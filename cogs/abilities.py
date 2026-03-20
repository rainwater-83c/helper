from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord

class Abilities(Cog):
    def __init__(self, bot):
        self.bot = bot

    abilities = app_commands.Group(
        name="abilities", 
        description="Abilities.",

        allowed_contexts=app_commands.AppCommandContext(
            guild=True, 
            dm_channel=True, 
            private_channel=True
        ),
        allowed_installs=app_commands.AppInstallationType(
            guild=True,
            user=True
        )
    )

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @abilities.command(name="red", description="Abilities to do with corruption.")
    @app_commands.choices(redability=[
        app_commands.Choice(name='Corrupt', value='corrupt'),
    ])
    async def red(self, interaction: discord.Interaction, user: discord.User)

    

async def setup(bot):
    await bot.add_cog(Main(bot))