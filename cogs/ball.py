from discord.ext import commands
import random

class BALL(commands.Cog):
    def __init__(self, client):
        self.client = client

   
    @commands.command(
        name='8ball',
        description='The say command',
        aliases=['8-ball', 'eightball'],
        usage='<text>')
    async def ball_command(self,ctx):
        # The 'usage' only needs to show the parameters
        # As the rest of the format is generated automatically

        # Lets see what the parameters are: -
        # The self is just a regular reference to the class
        # ctx - is the Context related to the command
        # For more reference - https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#context

        # Next we get the message with the command in it.
        msg = ctx.message.content

        # Extracting the text sent by the user
        # ctx.invoked_with gives the alias used
        # ctx.prefix gives the prefix used while invoking the command
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
             responses = ["It is certain.","It is decidedly so.",
             "Without a doubt.","Yes - definitely.","You may rely on it.",
             "As I see it, yes.","Most likely.","Outlook good.",
             "Yes.","Signs point to yes.","Reply hazy, try again.",
             "Ask again later.","Better not tell you now.",
             "Cannot predict now.","Concentrate and ask again.",
             "Don't count on it.","My reply is no.","My sources say no.",
             "Outlook not so good.","Very doubtful.",'yes','no','maybe'
                 ]
             await ctx.send(f'Question: {alias_used}\nAnswer: {random.choice      (responses)}')
             pass

        return


def setup(client):
    client.add_cog(BALL(client))