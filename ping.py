import discord
from discord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f"**🏓 Pong!** Bot latency is around __{round(self.bot.latency * 1000)}ms__")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs for Misc has been loaded!")

def setup(bot):
    bot.add_cog(PingCog(bot))