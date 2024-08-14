import discord
from discord.ext import commands
import random
from random import choice

class SimpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['simp'])
    async def simprate(self,ctx):
        simpembed = discord.Embed(title="Simprate Generator", description=f"You are {random.randint(0,100)}% simp!")
        simpembed.add_field(name="Simp much?", value="*Yea you do*")
        await ctx.send(embed=simpembed)

def setup(bot):
    bot.add_cog(SimpCog(bot))