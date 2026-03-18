import discord

def color_lore(colorname:str, color:hex, description:str, name:str, holder:str, element:str, abilities:list):
    embed = discord.Embed(
            title=colorname,
            description=description,
            colour=color
    )
    embed.add_field(name="Holder", value=holder, inline=True)
    embed.add_field(name="Representation", value=name, inline=True)
    embed.add_field(name="Element", value=element, inline=True)
    embed.add_field(name="Abilities", value='\n'.join(abilities), inline=False)
    embed.set_footer(text=f"{colorname} | {name} | {element}")
    return embed

def character_lore(colorname:str, color:hex, description:str, name:str, holder:str, element:str, abilities:list):
    embed = discord.Embed(
            title=colorname,
            description=description,
            colour=color
    )
    embed.add_field(name="Holder", value=holder, inline=True)
    embed.add_field(name="Representation", value=name, inline=True)
    embed.add_field(name="Element", value=element, inline=True)
    embed.add_field(name="Abilities", value='\n'.join(abilities), inline=False)
    embed.set_footer(text=f"{colorname} | {name} | {element}")
    return embed