import discord
from discord.ext import commands
import random
from random import choice

ppresponses = ['8D','8=D','8==D','8===D','8====D','8=====D','8======D','8=======D','8========D','8=========D','8==========D']


class PpCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(alisases=['pickle', 'penis', 'peepee'])
    async def pp(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        ppembed = discord.Embed(title='PP Size Machine', description= f"{user.mention}'s pp size")
        ppembed.add_field(name=(choice(ppresponses)), value="congrats?")
 
        await ctx.send(embed=ppembed)

def setup(bot):
    bot.add_cog(PpCog(bot))