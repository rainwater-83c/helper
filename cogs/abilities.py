from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO
from discord import app_commands
import discord

class Abilities(Cog):
    def __init__(self, bot):
        self.bot = bot

    red = app_commands.Group(
        name="red", 
        description="Red abilities.",

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

    yellow = app_commands.Group(
        name="yellow", 
        description="Yellow abilities.",

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

    green = app_commands.Group(
        name="green", 
        description="Green abilities.",

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

    cyan = app_commands.Group(
        name="cyan", 
        description="Cyan abilities.",

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

    blue = app_commands.Group(
        name="blue", 
        description="Blue abilities.",

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

    magenta = app_commands.Group(
        name="magenta", 
        description="Magenta abilities.",

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

    white = app_commands.Group(
        name="white", 
        description="White abilities.",

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

    black = app_commands.Group(
        name="black", 
        description="Black abilities.",

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

    # red abilities
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @red.command(name="corrupt", description="Corrupts something.")
    async def corrupt(self, interaction: discord.Interaction, thing: str):
        await interaction.response.send_message(f"{interaction.user.mention} corrupts {thing} with squares.")

    # yellow abilities
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @yellow.command(name="heat", description="Heats something.")
    async def heat(self, interaction: discord.Interaction, thing: str):
        await interaction.response.send_message(f"{interaction.user.mention} heats up {thing} by adding energy.")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @yellow.command(name="cool", description="Cools something.")
    async def cool(self, interaction: discord.Interaction, thing: str):
        await interaction.response.send_message(f"{interaction.user.mention} cools down {thing} by removing energy.")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @yellow.command(name="eletrocute", description="Eletrocutes something.")
    async def electrocute(self, interaction: discord.Interaction, thing: str):
        await interaction.response.send_message(f"{interaction.user.mention} electrocutes {thing}.")

    # green abilities
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @green.command(name="heal", description="Heals something.")
    async def heal(self, interaction: discord.Interaction, thing: str):
        await interaction.response.send_message(f"{interaction.user.mention} heals {thing}.")

    # cyan abilities
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @cyan.command(name="teleport", description="Teleports to someplace or teleports something to someplace.")
    async def teleport(self, interaction: discord.Interaction, thing: str, place: str):
        await interaction.response.send_message(f"{interaction.user.mention} teleports {thing} to {place}.")

    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @cyan.command(name="scale", description="Changes the size of something or yourself.")
    async def scale(self, interaction: discord.Interaction, thing: str, scale: int):
        await interaction.response.send_message(f"{interaction.user.mention} scales {thing} to {scale} times it's original size.")



async def setup(bot):
    await bot.add_cog(Main(bot))