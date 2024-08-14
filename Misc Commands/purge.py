import discord
from discord.ext import commands

class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clear'])
    async def purge(self, ctx, amount=10):
        amount = amount + 1
        if amount > 100:
            await ctx.send("Cannot purge more than 100 messages at a time.", delete_after=10)
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send(f"Purged **{amount - 1}** messages", delete_after=3)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs for Moderation has been loaded!")


def setup(bot):
    bot.add_cog(PurgeCog(bot))
