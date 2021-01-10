
from discord.ext import commands
import discord

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(
        name='kick',
        description='The kick command',
        aliases=['k']
    )
    async def kick_command(self,ctx, member : discord.Member, *, reason=None):
       await member.kick(reason=reason)

    @commands.command()
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
     
            if (user.name, user.discriminator) == (member_name,       member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')
                return
    

def setup(client):
    client.add_cog(Kick(client)) 
       