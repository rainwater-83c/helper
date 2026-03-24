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
            await interaction.followup.send(f"-# {user.name} has been pet {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="kiss", description="Gives a user a kiss")
    async def kiss(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('kiss', 0) + 1
            userfile['kiss'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} was kissed!\n-# {user.name} has been kissed {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="hug", description="Gives a user a hug")
    async def hug(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('hug', 0) + 1
            userfile['hug'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} was hugged!\n-# {user.name} has been hugged {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")


    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="cuddle", description="Cuddles a user.")
    async def cuddle(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('cuddle', 0) + 1
            userfile['cuddle'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} is being cuddled!\n-# {user.name} has been cuddled with {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="boop", description="Boops a user")
    async def boop(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('boop', 0) + 1
            userfile['boop'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} was booped!\n-# {user.name} has been booped {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="nuzzle", description="Boops a user")
    async def nuzzle(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('nuzzle', 0) + 1
            userfile['nuzzle'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} was nuzzled!\n-# {user.name} has been nuzzled {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="squish", description="Squishes a user")
    async def squish(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('squish', 0) + 1
            userfile['squish'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} was squished!\n-# {user.name} has been squished {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="hit", description="Hits a user")
    async def hit(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('hit', 0) + 1
            userfile['hit'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} got hit!\n-# {user.name} has been hit {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")


    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="punt", description="Punts a user")
    async def punt(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('punt', 0) + 1
            userfile['punt'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} got punted!\n-# {user.name} has been punted {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="bite", description="Bites a user")
    async def bite(self, interaction: discord.Interaction, user: discord.User):
        userfile = get_userfile(user.id, "interactions")
        if 'interact' not in userfile:
            # if unset, default for interactions to be enabled
            userfile['interact'] = True
            set_userfile(user.id, "interactions", json.dumps(userfile))
        if userfile['interact']:
            count = userfile.get('bite', 0) + 1
            userfile['bite'] = count
            set_userfile(user.id, "interactions", json.dumps(userfile))
            await interaction.response.send_message(f"{user.mention} got bitten!\n-# {user.name} has been bitten {count} time{'s' if count != 1 else ''}.")
        else:
            await interaction.response.send_message(f"{user.mention} does not have interactions enabled. No touchies!")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="gofuckyourself", description="Tells a user to go fuck themselves.")
    async def gofuckyourself(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"{user.mention}, you're being told to go fuck yourself!")

    
async def setup(bot):
    await bot.add_cog(Main(bot))