import discord
from discord.ext import commands
import random
from random import choice
import asyncio

class EightballCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *question):
        emb=discord.Embed(title=f'🎱 Answering {ctx.author}.. ', description='Let me think 🥱', color=ctx.author.color)
        emb.set_footer(text="My decision will be the best, don't sweat it")
        emb.set_thumbnail(url = ctx.author.avatar_url)
        msg = await ctx.send(embed=emb)

        ballresponses=['I would say go for it!', 'NO.', 'OF COURSE', 'My instincts tell me... No.', 'Bruh fuck yeaa', 'Nah', 'Tf you asking me for??', "I'm busy, go away", 'The Gods say yes.']
        ballembed=discord.Embed(title=f'Answer for {ctx.author}', description=f'**{choice(ballresponses)}**', color=ctx.author.color)
        ballembed.set_footer(text="Told ya, that will be $6.9")
        ballembed.set_thumbnail(url = ctx.author.avatar_url)

        await asyncio.sleep(2)
        await msg.edit(embed=ballembed)


    @eightball.error
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('<:error:899992500150865980> What do you want my answer for..')


def setup(bot):
    bot.add_cog(EightballCog(bot))
