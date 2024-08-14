import discord
from discord.ext import commands

class DmCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def dm(self, ctx, membr : discord.Member=None, *,messg):
        if membr == None:
            membr=ctx.author

        dmemb=discord.Embed(title=f'You\'ve got a Message from {ctx.author}!', description=f'{messg}', color=0xa6b7d7)
        dmemb.set_author(text='**NEW MESSAGE!!**')
        await membr.send(embed=dmemb)

def setup(bot):
    bot.add_cog(DmCog(bot))
