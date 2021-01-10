
import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import replit
import random

#client = commands.client(command_prefix= '.')
#
#  cogs   or mudule   or funtions
#

client = commands.Bot(command_prefix= '.')

cogs = ['cogs.pong','cogs.extent','cogs.kick','cogs.ball','cogs.embed','cogs.clear']

@client.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {client.user.name} - {client.user.id}')
    client.remove_command('help')
    # Removes the help command
    # Make sure to do this before loading the cogs
    for cog in cogs:
        client.load_extension(cog)
    return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

keep_alive()
#client.run(os.getenv('TOKEN'))

client.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
