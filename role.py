from discord.ext import commands
import discord
import os

intents =discord.Intents.default()
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.command()
async def register(ctx):
    await ctx.channel.send("Registration trying")

# bot.load_extension("main.py")
bot.run('OTMxNTQ0NTAwNDE1OTA5ODg4.YeF-bA.WvIyuTSZObXnLfuwIjqOBjcFz1g')