import discord
from discord.ext import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user:discord.Member=None):
        if user==None:
            user=ctx.author

        await ctx.send(f'{user.avatar_url}')


def setup(bot):
    bot.add_cog(AvatarCog(bot))
