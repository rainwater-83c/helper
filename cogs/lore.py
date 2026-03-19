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
    
    lore = app_commands.Group(
        name="lore", 
        description="Rain's lore.",

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
        green = color_lore('Green', 0x80ff80, "You can't exist without it.", 'Life', 'Fernwood', 'Earth', ['Able to control plants.', 'Able to give life to an object.'])
        cyan = color_lore('Cyan', 0x80ffff, "Makes up everything you see.", 'Space', 'Frostfeather', 'Ice', ['Able to teleport.', 'Able to control an object.', 'Able to change gravity.', 'Able to change the size of things.'])
        blue = color_lore('Blue', 0x8080ff, "They know what you're thinking.", 'Soul', 'Echosight', 'Water', ["Able to enter someone's mind.", "Able to view someone's intentions."])
        magenta = color_lore('Magenta', 0xff80ff, "Time is just a concept.", 'Time', 'Nightpool', 'Day/Night', ['Able to travel through time.', 'Able to take time through an object.', 'Able to pause time, speed up time, or slow time.'])
        white = color_lore('White', 0xffffff, "You can't have yin without yang.", 'Purity', 'Snowpelt', 'Light', ['Able to produce or control light.', 'Able to use any of the Red, Green, or Blue abilities.'])
        black = color_lore('Black', 0x808080, "You can't have yang without yin.", 'Void', 'Shadowleaf', 'Dark', ['Able to control the Void.', 'Able to use any of the Cyan, Magenta, or Yellow abilities.'])

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
        app_commands.Choice(name='Rainwater', value='u'),
        app_commands.Choice(name='Flamelight', value='r'),
        app_commands.Choice(name='Spirecloud', value='y'),
        app_commands.Choice(name='Fernwood', value='g'),
        app_commands.Choice(name='Frostfeather', value='c'),
        app_commands.Choice(name='Echosight', value='b'),
        app_commands.Choice(name='Nightpool', value='m'),
        app_commands.Choice(name='Snowpelt', value='w'),
        app_commands.Choice(name='Shadowleaf', value='k'),
    ])
    async def character(self, interaction: discord.Interaction, character: app_commands.Choice[str]):
        await interaction.response.defer()
        rain = character_lore("Rainwater", 0xffffff, "Niko infused with the power of color.", "Undefined", "Undefined", "Usually friendly.", "Very high", ["**Gender**: Undefined","**Species**: Not a cat", "**Eye color**: Undefined"])
        red = character_lore("Flamelight", 0xff8080, "Deputy of ThunderClan.", "Red", "Corruption", "Cold and unwelcoming.", "High", ["**Gender**: Male","**Species**: Feline", "**Coat color**: Ginger tabby", "**Eye color**: Red"])
        yellow = character_lore("Spirecloud", 0xffff80, "Warrior from WindClan.", "Yellow", "Energy", "Energetic and impatient", "Medium", ["**Gender**: Male", "**Species**: Feline", "**Coat color**: White", "**Eye color**: Yellow"])
        green = character_lore("Fernwood", 0x80ff80, "Medicine cat from SkyClan.", "Green", "Life", "Sympathetic and caring", "Medium", ["**Gender**: Female", "**Species**: Feline", "**Coat color**: Tortoiseshell", "**Eye color**: Green"])
        cyan = character_lore("Frostfeather", 0x80ffff, "Warrior from RiverClan.", "Cyan", "Space", "Friendly", "High", ["**Gender**: Male", "**Species**: Feline", "**Coat color**: White", "**Eye color**: Cyan"])
        blue = character_lore("Echosight", 0x8080ff, "Medicine cat from RiverClan.", "Blue", "Soul", "Mysterious and knowing", "Medium", ["**Gender**: Female", "**Species**: Feline", "**Coat color**: Gray tabby", "**Eye color**: Blue"])
        magenta = character_lore("Nightpool", 0xff80ff, "Medicine cat from ShadowClan.", "Magenta", "Time", "Shy", "Medium", ["**Gender**: Female", "**Species**: Feline", "**Coat color**: Gray tabby", "**Eye color**: Magenta"])
        white = character_lore("Snowpelt", 0xffffff, "Warrior from WindClan.", "White", "Purity", "Friendly", "High", ["**Gender**: Male", "**Species**: Feline", "**Coat color**: White", "**Eye color**: Heterochromatic; Red, green, and blue gradient in both eyes"])
        black = character_lore("Shadowleaf", 0x808080, "Warrior from ShadowClan.", "Black", "Void", "Mysterious", "High", ["**Gender**: Female", "**Species**: Feline", "**Coat color**: Black", "**Eye color**: Heterochromatic; Cyan, magenta, and yellow gradient in both eyes"])

        embed = None
        if character.value == 'u':
            embed = rain
        elif character.value == 'r':
            embed = red
        elif character.value == 'y':
            embed = yellow
        elif character.value == 'g':
            embed = green
        elif character.value == 'c':
            embed = cyan
        elif character.value == 'b':
            embed = blue
        elif character.value == 'm':
            embed = magenta
        elif character.value == 'w':
            embed = white
        elif character.value == 'k':
            embed = black
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Lore(bot))