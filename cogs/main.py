from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord
import json
from helpers.datafiles import make_userfile, get_userfile, set_userfile



class Main(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="petpet", description="Pets a user")
    async def petpet(self, interaction: discord.Interaction, user: discord.User):
        file = discord.File(BytesIO(requests.get(f'https://tt7homa.eu.pythonanywhere.com/petpet.gif?image={user.avatar.url}').content), filename=f'{user.id}_petpet.gif')
        await interaction.response.send_message(user.mention, file=file)

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="kiss", description="Gives a user a kiss")
    async def kiss(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        count = userfile.get('kiss', 0) + 1
        userfile['kiss'] = count
        set_userfile(user.id, "interactions", json.dumps(userfile))
        await interaction.response.send_message(f"{user.mention} was kissed!\n-# {user.name} has been kissed {count} times.")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="boop", description="Boops a user")
    async def boop(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        count = userfile.get('boop', 0) + 1
        userfile['boop'] = count
        set_userfile(user.id, "interactions", json.dumps(userfile))
        await interaction.response.send_message(f"{user.mention} was booped!\n-# {user.name} has been booped {count} times.")
    
    

    
async def setup(bot):
    await bot.add_cog(Main(bot))