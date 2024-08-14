import discord
from discord.ext import commands


class AmogusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='amogus', invoke_without_command=True)
    async def amogus(self, ctx):
        await ctx.channel.send("https://tenor.com/view/amogus-among-us-meme-impostor-sus-gif-20948491")

    @amogus.command(name='irl')
    async def irl_subcommand(self, ctx):
        await ctx.channel.send("https://tenor.com/view/among-among-us-in-real-life-gif-19770849")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs for Fun have been loaded!")

def setup(bot):
    bot.add_cog(AmogusCog(bot))