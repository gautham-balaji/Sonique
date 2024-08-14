import discord
from discord.ext import commands
import random

class HowgayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['gayrate', 'gayr8'])
    async def howgay(self, ctx, *, arg=None):
        if arg == None:
            arg = ctx.author.display_name
        grate = random.randint(0,100)
        em = {}
        if grate == 0:
            em="<:bar_start_empty:908685259871236137><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510>"
        if grate <= 10:
            em="<:bar_start_half:908696702721077288><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510>"
        if 10 < grate <= 20:
            em="<:bar_start_full:908684792613179442><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510> "
        if 20 < grate <= 30:
            em="<:bar_start_full:908684792613179442><:bar_half:908678961490444298><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510>"
        if 30 < grate <= 50:
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_empty:908679127463231518><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510>"
        if grate == 50:
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_half:908678961490444298><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510>"
        if 50 < grate <= 60:
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_empty:908679127463231518><:bar_end_empty:908684978416660510> "
        if 60 < grate <= 70:
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_half:908678961490444298><:bar_end_empty:908684978416660510>"
        if 70 < grate <= 80:
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_end_empty:908684978416660510>"
        if 80 < grate < 100 :
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_end_half:908697234705616957> "
        if grate == 100:
            em="<:bar_start_full:908684792613179442><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_full:908677789614497802><:bar_end_full:908684623675027478>"

        howgayembed = discord.Embed(title="Howgay Generator", description=f"{arg} is {grate}% gay!\n{em}", color=0xadd8e6)
        await ctx.send(embed=howgayembed) 



def setup(bot):
    bot.add_cog(HowgayCog(bot))
