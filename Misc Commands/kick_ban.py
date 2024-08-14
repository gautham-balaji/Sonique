import discord
from discord.ext import commands


class KickBanCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            reason="No reason given"
        await member.kick(reason=reason)
        await ctx.send(f'Kicked **{member}**')
        await member.send(f'You have been kicked from {ctx.guild.name} for: {reason}')

    @kick.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:error:899992500150865980> You need to mention someone to kick -_-")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:error:899992500150865980> You do not have permissions to kick users ;)")

    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if reason == None:
            reason="No reason given"
        await member.ban(reason=reason)
        await ctx.send(f'Banned **{member}**')
        await member.send(f'You have been banned from {ctx.guild.name} for: {reason}')

    @ban.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:error:899992500150865980> You need to mention someone to ban -_-")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:error:899992500150865980> You do not have permissions to ban users ;)")


    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs for Moderation has been loaded!")

def setup(bot):
    bot.add_cog(KickBanCog(bot))