
import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import replit

#client = commands.client(command_prefix= '.')
#
#  cogs   or mudule   or funtions
#

def get_prefix(client, message):

    prefixes = ['=']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['==']   # Only allow '==' as a prefix when in DMs

    # Allow users to @mention the bot instead of using a prefix when using a command.
    return commands.when_mentioned_or(*prefixes)(client, message)


client = commands.Bot(                                         
    # Create a new bot
    command_prefix=get_prefix,                              # Set the prefix
    description='A bot used for tutorial',                  # Set a description for the bot
    owner_id=374886124126208000,                            # Your unique User ID
    case_insensitive=True                                   # Make the commands case insensitive
)

#client = commands.Bot(command_prefix= '.')

#cogs = ['cogs.ping','cogs.extent','cogs.kick','cogs.ball','cogs.embed','cogs.clear','cogs.say']

@client.event
async def on_ready():
 #replit.clear()
 print(f'Logged in as {client.user.name} - {client.user.id}')
 client.remove_command('help')
 for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cog = f'cogs.{filename[:-3]}'
        client.load_extension(cog)   

#@bot.event
#async def on_ready():
#    replit.clear()
#    print(f'Logged in as {bot.user.name} - {bot.user.id}')
#    bot.remove_command('help')
#    # Removes the help command
#    # Make sure to do this before loading the cogs
#    for cog in cogs:
#        bot.load_extension(cog)
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

# if any error happens this event will be trigerd
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

# clear command without a defoult limit
@client.command()
async def clear_2(ctx, amount : int):
    await ctx.channel.purge(limit=amount)        

@clear_2.error
async def clear_2_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('PLease specify an amount of massages to delete.')

keep_alive()
#client.run(os.getenv('TOKEN'))

client.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
