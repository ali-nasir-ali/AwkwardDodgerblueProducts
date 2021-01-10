
from discord.ext import commands

class Inside(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is on online from inside cogs ')

def setup(client):
    client.add_cog(Inside(client))
    