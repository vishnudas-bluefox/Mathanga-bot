import discord
import random
from Data import Welcome
from discord.flags import Intents





intents = discord.Intents().default()
intents.members =True
client = discord.Client(intents=intents ) 



# select random message 
def WelcomeMessage():
    messages= Welcome.Welcome.message()
    return random.choice(messages)


# event for logged in comformation
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

# Welcome greeting
@client.event
async def on_member_join(member):
    guild = client.get_guild(931543683088658452)
    channel = guild.get_channel(931543683088658456)
    await channel.send("Welcome to this server mr {} ! :partying_face: ".format(member.mention)) # welcome on server 
    await member.send(str(WelcomeMessage()))

# Messsage test
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

client.run('OTMxNTQ0NTAwNDE1OTA5ODg4.YeF-bA.WvIyuTSZObXnLfuwIjqOBjcFz1g')