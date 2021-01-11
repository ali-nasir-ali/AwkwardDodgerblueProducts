
import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
import replit


def get_prefix(bot, message):

    prefixes = ['.']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['==']   # Only allow '==' as a prefix when in DMs

    # Allow users to @mention the bot instead of using a prefix when using a command.
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(                                         
    # Create a new bot
    command_prefix=get_prefix,                              # Set the prefix
    description='A bot used for tutorial',                  # Set a description for the bot
    owner_id=374886124126208000,                            # Your unique User ID
    case_insensitive=True                                   # Make the commands case insensitive
)

# case_insensitive=True is used as the commands are case sensitive by default

cogs = ['cogs.basic','cogs.embed']


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

@bot.event
async def on_ready():
 replit.clear()
 print(f'Logged in as {bot.user.name} - {bot.user.id}')
 bot.remove_command('help')
 for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        cog = f'cogs.{filename[:-3]}'
        bot.load_extension(cog)   

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('done')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('done')

# if any error happens this event will be trigerd
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

# clear command without a defoult limit
@bot.command()
async def clear_2(ctx, amount : int):
    await ctx.channel.purge(limit=amount)        

@clear_2.error
async def clear_2_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('PLease specify an amount of massages to delete.')

keep_alive()
#bot.run(os.getenv('TOKEN'))

bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
