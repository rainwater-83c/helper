from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord
import os
from helpers.datafiles import make_userfile, get_userfile, set_userfile

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
    
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @user.command(name="get", description="Gets a user's profile.")
    async def userget(self, interaction: discord.Interaction, user: discord.User):
        interactions = get_userfile(user.id, 'interactions')
        embed = discord.Embed(
            title=user.name,
            description=f'*meowww*',
            colour=0xffffff
        )
        interactions['kiss'] = interactions.get('kiss', 0)
        interactions['boop'] = interactions.get('boop', 0)
        interactions['hug'] = interactions.get('hug', 0)
        interactions['pet'] = interactions.get('pet', 0)
        interactions['cuddle'] = interactions.get('cuddle', 0)
        interactions['squish'] = interactions.get('squish', 0)
        interactions['hit'] = interactions.get('hit', 0)
        interactions['punt'] = interactions.get('punt', 0)
        
        embed.add_field(name="Interact?", value=interactions['interact'], inline=True)
        embed.add_field(name="Interaction stats:", value=f"Kiss: {interactions['kiss']}\nBoop: {interactions['boop']}\nHug: {interactions['hug']}\nPet: {interactions['pet']}\nCuddle: {interactions['cuddle']}\nHit: {interactions['hit']}\nPunt: {interactions['punt']}", inline=False)
        await interaction.response.send_message(embed=embed)
    

async def setup(bot):
    await bot.add_cog(UserProfile(bot))