#!/usr/bin/python3
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
from Data import Welcome
from discord.flags import Intents
import sqlite3
from dotenv import load_dotenv
import os



load_dotenv('.env')
intents = discord.Intents().default()
intents.members =True
client=commands.Bot(command_prefix="!",intents=intents)


# select random greeting messages for each user  
def WelcomeMessage():
    messages= Welcome.Welcome.message()
    return random.choice(messages)



# event for logged in comformation
@client.event
async def on_ready():

    db =sqlite3.connect('data.sqlite')      #create or check for database
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data(
            member_id INT,
            name TEXT
            )
    ''')
    print("Database = +ve")
    print("We have logged in as {0.user}".format(client))



#Send greeting messages for the newly joined members
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



# create role by Parameterised cammand [ex : !role Designer]
@client.command()
async def role(ctx,*args):
    try:
        user=ctx.author
        role=await ctx.guild.create_role(name=args[0])
        print(f'The {role} role was suscessfully created for {user}')
        await user.add_roles(role)
    except:
        await ctx.channel.send("Please double check the command [Ex: !role Designer] \n Try once more :🙂 ")




# Register names to database using parametrized command [ex: !register @testuser#4556]
@client.command()
async def register(ctx,user: discord.User):
    try:
        db = sqlite3.connect('data.sqlite')
    except:
        await ctx.channel.send("Bot can't connect to database now \nPlease Try Agin() ")
    cursor = db.cursor()

    cursor.execute(f"SELECT name FROM data WHERE member_id ={user.id}")
    result =cursor.fetchone()
    if result is None:
        sql =(" INSERT INTO data(member_id,name) VALUES(?,?)" )
        val1=(user.id,user.name)
        cursor.execute(sql,val1)
        await ctx.channel.send(f"The user succesfully added to the database \n Username:{user.name}\nUserID:{user}")

    else:
        await ctx.channel.send(f"The user already exist in the database \n Username:{user} \n Name:{user.name}")



    db.commit()
    cursor.close()
    db.close()


# role based data retrival [!names] "You have to create admin role first to acces this command"
@client.command()
@commands.has_role("admin") # This must be exactly the name of the appropriate role
async def names(ctx):
    db = sqlite3.connect('data.sqlite')
    cursor = db.cursor()


    cursor.execute(f"SELECT name FROM data")
    result =cursor.fetchall()
    for i in result:        #using two for loops for get rid of the braces from sqlite3
        for j in i:
            await ctx.channel.send(j)


    cursor.close()
    db.close()

# error handling session "Error Handling " [For now there is no error handling just wait for little more time :)]
@client.event
async def on_comman_error(ctx,error):
    pass
Token = os.getenv('username')
client.run(Token)

