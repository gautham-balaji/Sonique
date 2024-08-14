import discord
from discord.ext import commands
import random
from random import choice

roast_responses = ['If I had a face like yours, I would sue my parents', 'Man, I found your nose... IN MY FUCKIN BUSINESS', 'My middle finger gets a boner when I see you', 'My iPhone battery lasts longer than one of your relationships', 'You know, you should use gluesticks instead of chapsticks', 'Man you made a Happy Meal cry :(', 'OMG IT KNOWS HOW TO RUN A COMMAND, GET THE CAMERA 📸']

class RoastCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command(aliases=['roastme'])
    async def roast(self, ctx):
        await ctx.send(choice(roast_responses))

def setup(bot):
    bot.add_cog(RoastCog(bot))