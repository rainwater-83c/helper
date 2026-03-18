from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord
from helpers.embeds import color_lore, character_lore

class Lore(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    lore = app_commands.Group(name="lore", description="Rain's lore.")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @lore.command(name="color", description="Gets the lore of a color.")
    @app_commands.choices(color=[
        app_commands.Choice(name='Red', value='r'),
        app_commands.Choice(name='Yellow', value='y'),
        app_commands.Choice(name='Green', value='g'),
        app_commands.Choice(name='Cyan', value='c'),
        app_commands.Choice(name='Blue', value='b'),
        app_commands.Choice(name='Magenta', value='m'),
        app_commands.Choice(name='White', value='w'),
        app_commands.Choice(name='Black', value='k'),
    ])
    async def color(self, interaction: discord.Interaction, color: app_commands.Choice[str]):
        await interaction.response.defer()
        red = color_lore('Red', 0xff8080, 'The evil one.', 'Corruption', 'Flamelight', 'Fire', ['Able to corrupt anything with squares.', 'Able to light things on fire.'])
        yellow = color_lore('Yellow', 0xffff80, "It's the small things that matter.", 'Energy', 'Spirecloud', 'Eletricity', ['Able to control the flow of eletricity.', 'Able to control the amount of electrons in atoms.'])
        green = color_lore('Green', 0x80ff80, "", 'Life', 'Fernwood', 'Earth', ['Able to control plants.', 'Able to give life to an object.'])
        cyan = color_lore('Cyan', 0x80ffff, "Makes up everything you see.", 'Space', 'Frostclaw', 'Ice', ['Able to teleport.', 'Able to control an object.', 'Able to change gravity.', 'Able to change the size of things.'])
        blue = color_lore('Blue', 0x8080ff, "They know what you're thinking.", 'Soul', 'Echosight', 'Water', ['Able to enter someone's mind.', 'Able to view someone's intentions.'])
        magenta = color_lore('Magenta', 0xff80ff, "Time is just a concept.", 'Time', 'Nightpool', 'Day/Night', ['Able to travel through time.', 'Able to take time through an object.', 'Able to pause time, speed up time, or slow time.'])
        white = color_lore('White', 0xffffff, "You can't have yin without yang.", 'Purity', 'Snowpelt', 'Light', ['Able to produce or control light.', 'Able to use any of the Red, Green, or Blue abilities.'])
        black = color_lore('Black', 0x000000, "You can't have yang without yin.", 'Void', 'Shadowleaf', 'Dark', ['Able to control the Void.', 'Able to use any of the Cyan, Magenta, or Yellow abilities.'])

        embed = None
        if color.value == 'r':
            embed = red
        elif color.value == 'y':
            embed = yellow
        elif color.value == 'g':
            embed = green
        elif color.value == 'c':
            embed = cyan
        elif color.value == 'b':
            embed = blue
        elif color.value == 'm':
            embed = magenta
        elif color.value == 'w':
            embed = white
        elif color.value == 'k':
            embed = black
        await interaction.followup.send(embed=embed)

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @lore.command(name="character", description="Gets the lore of a character.")
    @app_commands.choices(character=[
        app_commands.Choice(name='Flamelight', value='r'),
        app_commands.Choice(name='Spirecloud', value='y'),
        app_commands.Choice(name='Fernwood', value='g'),
        app_commands.Choice(name='Frostclaw', value='c'),
        app_commands.Choice(name='Echosight', value='b'),
        app_commands.Choice(name='Nightpool', value='m'),
        app_commands.Choice(name='Snowpelt', value='w'),
        app_commands.Choice(name='Shadowleaf', value='k'),
    ])
    async def character(self, interaction: discord.Interaction, character: app_commands.Choice[str]):
        red = character_lore("Flamelight", 0xff8080, "", "Red", "Corruption", "", "", [])
async def setup(bot):
    await bot.add_cog(Lore(bot))