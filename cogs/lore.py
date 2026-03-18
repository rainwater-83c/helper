from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord

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
        red = discord.Embed(
            title="Red",
            description="Red",
            colour=0xff8080
        )
        red.add_field(name="Holder", value="Flamelight", inline=True)
        red.add_field(name="Representation", value="Corruption", inline=True)
        red.add_field(name="Element", value="Fire", inline=True)
        red.add_field(name="Abilities", value="Able to corrupt anything with squares.\nAble to light things on fire.", inline=False)
        red.set_footer(text="Red | Corruption | Fire")

        yellow = discord.Embed(
            title="Yellow",
            description="Yellow",
            colour=0xffff80
        )
        yellow.add_field(name="Holder", value="Spirecloud", inline=True)
        yellow.add_field(name="Representation", value="Energy", inline=True)
        yellow.add_field(name="Element", value="Eletricity", inline=True)
        yellow.add_field(name="Abilities", value="Control the flow of eletricity.\nControl the amount of electrons in atoms.", inline=False)
        yellow.set_footer(text="Yellow | Energy | Eletricity")

        green = discord.Embed(
            title="Green",
            description="Green",
            colour=0x80ff80
        )
        green.add_field(name="Holder", value="Fernwood", inline=True)
        green.add_field(name="Representation", value="Life", inline=True)
        green.add_field(name="Element", value="Earth", inline=True)
        green.add_field(name="Abilities", value="Able to control plants.\nAble to give life to an object.", inline=False)
        green.set_footer(text="Green | Life | Earth")

        cyan = discord.Embed(
            title="Cyan",
            description="Cyan",
            colour=0x80ffff
        )
        cyan.add_field(name="Holder", value="???", inline=True)
        cyan.add_field(name="Representation", value="Space", inline=True)
        cyan.add_field(name="Element", value="Ice", inline=True)
        cyan.add_field(name="Abilities", value="Able to teleport.\nAble to control an object.", inline=False)
        cyan.set_footer(text="Cyan | Matter | Ice")

        blue = discord.Embed(
            title="Blue",
            description="Blue",
            colour=0x8080ff
        )
        blue.add_field(name="Holder", value="Echosight", inline=True)
        blue.add_field(name="Representation", value="Soul", inline=True)
        blue.add_field(name="Element", value="Water", inline=True)
        blue.add_field(name="Abilities", value="Able to enter someone's mind.\nAble to view someone's intentions.", inline=False)
        blue.set_footer(text="Blue | Soul | Water")

        magenta = discord.Embed(
            title="Magenta",
            description="Magenta",
            colour=0xff80ff
        )
        magenta.add_field(name="Holder", value="Nightpool", inline=True)
        magenta.add_field(name="Representation", value="Time", inline=True)
        magenta.add_field(name="Element", value="Day/Night", inline=True)
        magenta.add_field(name="Abilities", value="Able to travel through time.\nAble to take time through an object.\nAble to pause time, speed up time, or slow time.", inline=False)
        magenta.set_footer(text="Magenta | Time | Day/Night")

        white = discord.Embed(
            title="White",
            description="White",
            colour=0xffffff
        )
        white.add_field(name="Holder", value="???", inline=True)
        white.add_field(name="Representation", value="Purity", inline=True)
        white.add_field(name="Element", value="Light", inline=True)
        white.add_field(name="Abilities", value="Able to produce or control light.\nAble to use any of the Red, Green, or Blue abilities.", inline=False)
        white.set_footer(text="White | Purity | Light")

        black = discord.Embed(
            title="Black",
            description="Black",
            colour=0x000000
        )
        black.add_field(name="Holder", value="???", inline=True)
        black.add_field(name="Representation", value="Void", inline=True)
        black.add_field(name="Element", value="Dark", inline=True)
        black.add_field(name="Abilities", value="Able to control the Void.\nAble to use any of the Cyan, Magenta, or Yellow abilities.", inline=False)
        black.set_footer(text="Black | Void | Dark")


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

async def setup(bot):
    await bot.add_cog(Lore(bot))