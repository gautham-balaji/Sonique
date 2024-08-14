import discord
from discord.ext import commands

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx, title, *,desc):
        cmdembed=discord.Embed(title=title, color=ctx.author.color, description=desc)
        await ctx.channel.send(embed=cmdembed)


    @embed.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('<:error:899992500150865980> You need to give me a **Title** (in quotes " "), and a **Description**. For example: `?embed "This is an Embed Title" This is the description of this embed` will send:')
        embed=discord.Embed(title='This is an Embed Title', description='This is the description of this embed')
        await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:error:899992500150865980> You do not have permissions to send embeds ;)")

def setup(bot):
    bot.add_cog(EmbedCog(bot))
