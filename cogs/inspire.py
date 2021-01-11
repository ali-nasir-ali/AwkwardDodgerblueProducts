
import discord
from discord.ext import commands
import requests
import json


class Inspire(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(
        name='inspire',
        description='The inspire command',
        aliases=['in']
    )
    async def inspire_command(self, ctx):
      response = requests.get("https://zenquotes.io/api/random")
      json_data = json.loads(response.text)
      quote = json_data[0]['q'] + " -" + json_data[0]['a']
      await ctx.send(quote)

def setup(client):
    client.add_cog(Inspire(client))
