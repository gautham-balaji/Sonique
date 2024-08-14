import discord
from discord.ext import commands
from discord import Embed

help = discord.Embed(title="Help", description= f"Use `[p]help <category>` for more information on the commands!")
help.add_field(name = "Music", value=f"Run `[p]help music` or click the 'Music' Button for more information!", inline=True)
help.add_field(name= "Fun", value= "howgay, pp, simp, joke, amogus and SO MUCH MORE!", inline=True)
help.add_field(name= "Moderation", value= "Ban, Kick, Purge", inline=True)
help.add_field(name= "Giveaway", value="Coming real soon", inline=True)
help.set_footer(text="Note: [p] refers to the server's prefix!")

music = discord.Embed(title= "Music Commands", description= "All the Music commands you can use!")
music.add_field(name= "▪︎ connect", value="Connects to the VC you are in *ALIAS con*", inline=True)
music.add_field(name= "▪︎ disconnect", value="Disconnects from the VC *ALIAS vc*", inline=True)
music.add_field(name= "▪︎ play <query>",value="Plays the requested query or queues it", inline=True)
music.add_field(name= "▪︎ skip", value= "Skips to the next queued song", inline=True)
music.add_field(name= "▪︎ pause", value="Paused the song", inline=True)
music.add_field(name= "▪︎ resume", value="Resumes paused music", inline=True)
music.add_field(name= "▪︎ seek <seconds>", value="Skips the song the requested amount", inline=True)
music.add_field(name= "▪︎ volume <0-100>", value="Increaes/Decreases the volume *ALIAS vol*", inline=True)
music.add_field(name= "▪︎ loop <type>", value="Loop either the **playlist**(queue), **track** or **none**", inline=True)
music.add_field(name= "▪︎ nowplaying", value="Displays the current song playing", inline=True)
music.add_field(name= "▪︎ queue", value="Displays the song queue *ALIAS q*", inline=True)
music.add_field(name= "▪︎ equalizer", value="Boost you music! *ALIAS eq*", inline=True)
music.set_footer(text=f"Please do use the prefix before each command!")

fun = discord.Embed(title='Fun commands!', description = 'A little something you can have fun with ;)')
fun.add_field(name=  "howgay", value='See how gay you are!', inline=True)
fun.add_field(name='pp', value="Get your pp size 😳", inline=True)
fun.add_field(name="simp", value="Find out how big of a simp you are", inline=True)
fun.add_field(name='joke', value='Get a random ~~terrible~~ good joke', inline=True)
fun.add_field(name="amogus", value= "amogus. ↭ `amogus irl` for some IRL amogus ;)", inline=True)
fun.set_footer(text=f"Please do use the prefix before each command!")

misc=discord.Embed(title='Misc commands', description='Misccc commmaandds')


mod=discord.Embed(title='Mod commands', description='Mod commands')

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cry(self, ctx):
        contents = [
        help, music, fun, misc, mod
    ]
        pages = 5
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page - 1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)

            except:
                break

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs for Help has been loaded!")

def setup(bot):
    bot.add_cog(HelpCog(bot))

'''buttons = ButtonsClient(client)

@client.group(name='help', invoke_without_command=True)
async def Help(ctx):
    msg = await buttons.send(
		content=None,
        embed = help,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "Music",
					custom_id = "musicbutton",

				),

				Button(

            
					style = ButtonType().Success,
					label = "Fun!",
					custom_id = "funbutton",
                                    
				),

				Button(
					style = ButtonType().Danger,
					label = "Moderation",
					custom_id = "modbutton",
				),
				Button(
					style = ButtonType().Secondary,
					label = "Giveaway",
					custom_id = "gawbutton",
				)
			])
		]
	)
 
    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel
    

    try:
           res = await client.wait_for("button_click", check=check, timeout=30)
    except asyncio.exceptions.TimeoutError:
       

        return
    if res.component.label == 'Music':
        await msg.edit(content='Music Commands!', embed=music)
        return

    if res.component.label == 'Fun!': 
        await res.respond(content = 'Fun Commands!', embed=fun)
        return

    
@Help.command(name = 'music')
async def music_subcommand(ctx):
    await ctx.channel.send(embed=music)

@Help.command(name = 'fun')
async def fun_subcommand(ctx):
    await ctx.channel.send(embed=fun)'''
