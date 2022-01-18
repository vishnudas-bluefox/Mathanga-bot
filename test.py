from discord.ext import commands
from Data import Welcome
import discord
import random

client=commands.Bot(command_prefix=".")


# select random message 
def WelcomeMessage():
    messages= Welcome.Welcome.message()
    return random.choice(messages)



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


# notify on reactions
@client.event
async def on_raw_reaction_add(reaction):
    channel=client.get_channel(reaction.channel_id)
    channel2=client.get_channel(931791895909269514)
    message=await channel.fetch_message(reaction.message_id)
    emoji=reaction.emoji.name
    await channel2.send(f"{reaction.member.name} reacted to {message.author.name}'s message {emoji}")

# role by Parameterised cammand
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


client.run('OTMxNTQ0NTAwNDE1OTA5ODg4.YeF-bA.WvIyuTSZObXnLfuwIjqOBjcFz1g')