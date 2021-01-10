
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(
        name='clear',
        description='The clear command',
        aliases=['c']
    )
    async def clear_command(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Clear(client))
    