import discord
from discord.ext import commands
import random
from random import choice

jokes = [ 'Why don’t oysters donate to charity? Because they’re shellfish.',
'What does a baby computer call its father? Data.',
'What did the custodian say when he jumped out of the closet? “Supplies!”',
'Why are colds bad criminals? Because they’re easy to catch.',
'How does a penguin build its house? Igloos it together.',
'Which knight invented King Arthur’s Round Table? Sir Cumference.',
'What do sprinters eat before a race? Nothing. They fast.',
'What do you call a fly without wings? A walk!',
'What happens when you witness a ship wreck? You let it sink in.',
'How can you find Will Smith in the snow? Follow the fresh prints.',
'What does a clock do when it’s hungry? It goes back four seconds.',
'What’s the easiest way to make a glow worm happy? Cut off its tail—it’ll be delighted!',
'What do you call a belt made of watches? A waist of time!',
'Why did Adele cross the road? To say hello from the other side!',
'What’s the best way to carve wood? Whittle by whittle.',
'What did the teacher do with the student’s report on cheese? She grated it.',
'What’s the difference between a piano and a fish? You can tune a piano, but you can’t tuna fish.',
'What did the pirate say on his 80th birthday? “Aye, matey!”',
'How do you organize an astronomer’s party? You planet.',
'What’s the action like at a circus? In-tents.']

class JokesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        await ctx.send(choice(jokes))

def setup(bot):
    bot.add_cog(JokesCog(bot))
