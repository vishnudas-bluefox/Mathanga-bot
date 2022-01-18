from discord.ext import commands


client=commands.Bot(command_prefix=".")
class roles:

    def role_assign():

        # role by Parameterised cammand
        @client.command()
        async def ping(ctx):
            await ctx.send("Pong!")


# Messsage test
@client.event
async def on_message(message,*args,**kwargs):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$role"):
        role = str(args)
        await message.channel.send(role)
