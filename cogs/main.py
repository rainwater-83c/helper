from discord.ext.commands import Cog
from PIL import Image, ImageSequence
import requests
from io import BytesIO




class Main(Cog):
    def __init__(self, bot):
        self.bot = bot

    def gif_overlay(image, gif)
        buffer = BytesIO()
        frames = []
        for frame in ImageSequence.Iterator(gif):
            output = image.copy()
            frame_px = frame.load()
            output_px = output.load()
            transparent_foreground = frame.convert('RGBA')
            transparent_foreground_px = transparent_foreground.load()
            for x in range(frame.width):
                for y in range(frame.height):
                    if frame_px[x, y] in (frame.info["background"], frame.info["transparency"]):
                        continue
                    output_px[x, y] = transparent_foreground_px[x, y]
            frames.append(output)

        frames[0].save(buffer, format="GIF", save_all=True, append_images=frames[1:]) 
        gif_bytes = buffer.getvalue()
        buffer.close()
        
        

    
    @app_commands.allowed_installs(users=True, guilds=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="petpet", description="Pets a user")
    async def petpet(self, interaction: discord.Interaction, user: discord.User):
        avatar = user.avatar.url
        img = Image.open(BytesIO(requests.get(avatar))
        interaction.response.send_message("")
    
async def setup(bot):
    await bot.add_cog(Main(bot))