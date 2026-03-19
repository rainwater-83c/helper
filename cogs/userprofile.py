from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord
import os

class UserProfile(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.users = []

    def update_choices(self):
        appchoices = []
        for uid in [f for f in os.listdir("data/users")]:
            user = self.bot.get_user(uid)
            appchoices.append(app_commands.Choice(name=user.name, value=user.id)),
        

    user = app_commands.Group(
        name="user", 
        description="Users.",

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
    
    #@app_commands.allowed_installs(users=True, guilds=True)
    #@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    #@user.command(name="get", description="Gets a user's profile.")

async def setup(bot):
    await bot.add_cog(UserProfile(bot))