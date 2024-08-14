import discord
from discord.ext import commands

class SiUiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['si'])
    async def serverinfo(self, ctx,):
        embed = discord.Embed(title=f"Server Information for {ctx.guild.name}", color=0xa6b7d7)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        embed.set_thumbnail(url = str(ctx.guild.icon_url))
        embed.add_field(name="<:smallbluearrow:895275925921464350> Server Owner", value=f"<a:Arrow:895278191911010314> {ctx.guild.owner} | {ctx.guild.owner.mention}", inline=False)
        embed.add_field(name="<:smallbluearrow:895275925921464350> Members", value=f"<a:Arrow:895278191911010314> {ctx.guild.member_count}", inline=False)
        embed.add_field(name="<:smallbluearrow:895275925921464350> Channels", value=f"<a:Arrow:895278191911010314> **{channels}** | {text_channels} Text Channels, {voice_channels} Voice Channels", inline=False)
        embed.add_field(name="<:smallbluearrow:895275925921464350> Categories", value=f"<a:Arrow:895278191911010314> {categories}", inline=False)
        embed.add_field(name="<:smallbluearrow:895275925921464350> Server ID", value=f"<a:Arrow:895278191911010314> {ctx.guild.id}", inline=False)
        await ctx.send(embed=embed)


    @commands.command(aliases=['ui', 'whois', 'wi'])
    async def userinfo(self, ctx, memb : discord.Member=None):
        if memb == None:
            memb=ctx.author
        userembed = discord.Embed(colour=memb.color)
        userembed.set_author(name=f'User info for {memb}')
        userembed.set_thumbnail(url = memb.avatar_url)
        userembed.add_field(name="<:smallbluearrow:895275925921464350> ID", value=f"<a:Arrow:895278191911010314> {memb.id}",inline=False)
        userembed.add_field(name="<:smallbluearrow:895275925921464350> Name", value=f"<a:Arrow:895278191911010314> {memb}", inline=False)
        userembed.add_field(name="<:smallbluearrow:895275925921464350> Created At", value=f"<a:Arrow:895278191911010314> {memb.created_at}", inline=False)
        userembed.add_field(name="<:smallbluearrow:895275925921464350> Joined At", value=f"<a:Arrow:895278191911010314> {memb.joined_at}", inline=False)
        userembed.add_field(name="<:smallbluearrow:895275925921464350> Bot?", value=f"<a:Arrow:895278191911010314> {memb.bot}", inline=False)
        userembed.add_field(name='<:smallbluearrow:895275925921464350> Top Role', value=f'<a:Arrow:895278191911010314> {memb.top_role.mention}', inline=False)


        await ctx.send(embed=userembed)


def setup(bot):
    bot.add_cog(SiUiCog(bot))