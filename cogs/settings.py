from discord.ext.commands import Cog
from discord.ext import commands
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord
from helpers.datafiles import make_userfile, get_userfile, set_userfile
import json

class Settings(Cog):
    def __init__(self,bot):
        self.bot = bot

    settings = app_commands.Group(
        name="setting", 
        description="Settings for users and the bot.",

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

    @commands.is_owner()
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @settings.command(name="interaction", description="Changes someone's interaction preferences")
    async def interaction(self,interaction: discord.Interaction,user: discord.User, enabled: bool):
        userfile = get_userfile(user.id, "interactions")
        userfile['interact'] = enabled
        set_userfile(user.id, "interactions", json.dumps(userfile))
        await interaction.response.send_message(f"{user.mention}'s preferences set to {'interact.' if enabled else 'do not interact.'}")

async def setup(bot):
    await bot.add_cog(Settings(bot))