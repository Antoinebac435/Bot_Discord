import discord
from discord import Intents

intents = Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if "quoi" in message.content.lower():
        await message.channel.send("feur")
    if "pourquoi" in message.content.lower():
        await message.channel.send("parce que feur")
        
        
client.run("MTA1OTg2OTA2ODI1OTI0NjIxMA.G5OmOG.37WYxSkfErAwkunJRkyjPP5lj_JXB9Er--Fauw")
