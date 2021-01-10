
import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import replit

#client = commands.client(command_prefix= '.')
#
#  cogs   or mudule   or funtions
#

client = commands.Bot(command_prefix= '.')

cogs = ['cogs.ping','cogs.extent','cogs.kick','cogs.ball','cogs.embed','cogs.clear','cogs.say']


for filename in os.listdir('./cogs'):
    replit.clear()
    client.remove_command('help')
    if filename.endswith('.py'):
        cog = f'cogs.{filename[:-3]}'
        client.load_extension(cog)   

#@client.event
#async def on_ready():
#    replit.clear()
#    #client.remove_command('help')
#    # Removes the help command
#    # Make sure to do this before loading the cogs
#    for cog in cogs:
#        client.load_extension(cog)
#    return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('done')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('done')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('done')


keep_alive()
#client.run(os.getenv('TOKEN'))

client.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
