import discord
from discord.ext import commands

class Say(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(
        name='say',
        description='The say command',
        aliases=['repeat', 'parrot'],
        usage='<text>'
    )
    async def say_command(self, ctx):
        
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        # Next, we check if the user actually passed some text
        if text == '':
            # User didn't specify the text

            await ctx.send(content='You need to specify the text!')

            pass
        else:
            # User specified the text.

            await ctx.send(content=f"**{text}**")

            pass

        return


def setup(client):
    client.add_cog(Say(client))