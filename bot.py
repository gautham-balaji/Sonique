'''All Imports needed.'''
import discord
from discord.state import logging_coroutine
from discord import app_commands
from discord.ext.commands.core import command
from discord import activity, channel, client, colour, embeds, emoji, guild, member, message, user
from discord.flags import Intents
from discord import Embed
from discord.ext.commands import Greedy
from discord import User
import asyncio
import socket
import os
import logging
import struct
import threading
from discord_components.ext.filters import guild_filter
from discord_ui import SlashedCommand, Button, UI
from discord_ui import components
from discord_ui.components import LinkButton
import collection
from discord.utils import get
from discord_components.dpy_overrides import fetch_message
import dismusic
import datetime
import random
from random import choice
from random import randint
from discord.ext import commands, tasks
from discord.ext.commands import bot, has_permissions, MissingPermissions, when_mentioned_or
import json
from discord_components import *
from discord_buttons_plugin import *
from collection import *
import distutils
from distutils import *
import urllib
from typing import Optional, Set
from test import *


########################################################################################################



''' For the 'prefix' command (get prefix, default prefix on leave/join, etc)'''

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]





intents= discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix =get_prefix, intents=intents)
client.remove_command("help")
ui = UI(client)


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '?'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] =  prefix
    

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f"Succesfully changed prefix to **{prefix}**")


    

@prefix.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:error:899992500150865980> Mate, you didn't tell me what to change the prefix to.")






class Groups(commands.Cog):

  def __init__(self, bot):
    self.bot=bot


  @commands.Cog.listener()
  async def on_ready(self):
      print("Subcommands Cog has been loaded\n-----")

'''^^ + som cogs'''

##################################################################################################################


buttons = ButtonsClient(client)



#############################################################################################################
  
    


'''Lava nodes info'''

client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'main',
        'password': 'anything',
        'region': 'singapore'
    }
]





















#############################################################################################################
'''Only Support Server Command ig'''
'''Verify Command'''


@client.command()
async def verify(ctx):
            if ctx.guild.id != 893472918519029760:
                await ctx.send('This command can be used only in the Support Server.')
            else:
    
                em = discord.Embed(title=f'Verification for {ctx.guild.name}',
                       description = "**After reading #rules**, click the 'Verify' button to verify yourself")

            msg = await buttons.send(
                            content=None,
                            channel=ctx.channel.id,
                            embed = em,
                        components=[
                            ActionRow([
                                  Button(
                                      style=ButtonType().Danger,
                                      label='No thanks',
                                      custom_id='noverify'
                                  ),
                                
                                  Button(
                                      style=ButtonType().Success,
                                      label='Verify',
                                      custom_id='verifybutton'
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
            if res.component.label == 'No thanks':
                await res.respond(content='Ok, suit yourself.')
                return

            if res.component.label == 'Verify':
                member = ctx.author
                mrole = discord.utils.find(
                lambda r: r.name == 'Members', ctx.message.guild.roles
        )
                role = get(member.guild.roles, name = 'Members')
                if mrole in member.roles:
                    await res.respond(content='You are already verified')
                    return
                else:
                    await member.add_roles(role)
                    await res.respond(content='You have been verified!')
                    return
            else:
                return


#############################################################################################################

@client.command('role')
@commands.has_permissions(manage_roles=True) 
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position:
    return await ctx.send('<:error:899992500150865980> That role is above your top role!') 
  if role.position > client.top_role.position:
     return await ctx.send('<:error:899992500150865980> I am not high enough in the hierarchy for that role.')
  if role in user.roles:
      await user.remove_roles(role) 
      await ctx.send(f"Removed **{role}** from **{user}**")
  else:
      await user.add_roles(role)
      await ctx.send(f"Added **{role}** to **{user}**") 


@role.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('<:error:899992500150865980> You need to specify a user and a role.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('<:error:899992500150865980> You do not have permissions to use that command')














    










#############################################################################################################
'''Button Role command'''



#############################################################################################################
'''F1 Command'''

@client.group(name='formulaone', invoke_without_command=True, aliases=['f1', 'formula1', 'fone'], case_insensitive=False)
async def formulaone(ctx):
    fembed=discord.Embed(title='Formula One 2021 Standings', url = 'https://www.formula1.com/en/results.html/2021/drivers.html', color=ctx.author.color)
    fembed.add_field(name='<:gold:901409567810940938> Max Verstappen <:LineYellow:898164232284164118> 287.5', value='<:smallbluearrow:895275925921464350 **8 Wins**, 13 Podiums', inline=False)
    fembed.add_field(name='<:silver:901409597837967360> Lewis Hamilton <:LineYellow:898164232284164118> 275.5', value='<:smallbluearrow:895275925921464350 **5 Wins**, 12 Podiums', inline=False)
    fembed.add_field(name='<:bronze:901409640808611850> Valterri Bottas <:LineYellow:898164232284164118> 185', value='<:smallbluearrow:895275925921464350> **1 Win**, 9 Podiums', inline=False)
    fembed.add_field(name='4️⃣ Sergio Perez <:LineYellow:898164232284164118> 150', value='<:smallbluearrow:895275925921464350> **1 Win**, 4 Podiums', inline=False)
    fembed.add_field(name='5️⃣ Lando Norris <:LineYellow:898164232284164118> 149', value='<:smallbluearrow:895275925921464350 **0 Wins**, 4 Podiums', inline=False)
    fembed.add_field(name='6️⃣ Charles Leclerc <:LineYellow:898164232284164118> 128', value='<:smallbluearrow:895275925921464350 **0 Wins**, 1 Podium', inline=False)
    fembed.add_field(name='7️⃣ Carlos Sainz <:LineYellow:898164232284164118> 122.5', value='<:smallbluearrow:895275925921464350 **0 Wins**, 3 Podiums', inline=False)
    fembed.add_field(name='8️⃣ Daniel Ricciardio <:LineYellow:898164232284164118> 105', value='<:smallbluearrow:895275925921464350> **1 Win**, 1 Podium', inline=False)
    fembed.add_field(name='9️⃣ Pierre Gasly <:LineYellow:898164232284164118> 74', value='<:smallbluearrow:895275925921464350 **0 Wins**, 1 Podium', inline=False)
    fembed.add_field(name='🔟 Fernando Alonso <:LineYellow:898164232284164118> 58', value='<:smallbluearrow:895275925921464350 **0 Wins**, 0 Podiums', inline=False)
    fembed.add_field(name='Next Race:', value='[Mexico City Grand Prix](https://www.formula1.com/content/fom-website/en/racing/2021/Mexico.html)')
    fembed.set_author(name='Previous Race: United States Grand Prix - 🏆 Max Verstappen',url='https://youtu.be/-Ee08uFurok')
    fembed.set_thumbnail(url='https://1000logos.net/wp-content/uploads/2021/06/F1-logo.png')
    fembed.set_footer(text="Run '?f1 info' for more info on commands like most wins, most poles, etc!")
    await ctx.send(embed=fembed)


@formulaone.group(name='most', invoke_without_command=True)
async def most_subcommand(ctx):
    mostembed=discord.Embed(title='Want to see more things?', description='wins**, **poles**, **championships**, **DNFs**, **Fastest-laps** are the options you can choose to view more information about Formula One!')
    mostembed.add_field(name='Additionally..', value='You can also use a hyphen (-). For example `[p]f1 most-wins`')
    mostembed.set_author(name='Formula One', icon_url=ctx.author.avatar_url)
    mostembed.set_footer(text="Please do use 'most' before each option! ex: [p]f1 most wins")
    mostembed.add_field(name='More Information on Formula Racing', value='[Formula 2](https://www.fiaformula2.com/)\n[Formula 3](https://www.fiaformula3.com/)\n[Formula E](https://www.fiaformulae.com/)')
    await ctx.send(embed=mostembed)

@most_subcommand.command(name='wins')
async def win_subcommand(ctx):
    winembed=discord.Embed(title='Most Wins in Formula 1',  description='This is the list of the drivers who have the most wins in F1 history')
    winembed.add_field(name='<:gold:901409567810940938> :flag_gb: Lewis Hamilton',value='<:line:903128366054510602><:arr:902911455664414760> **100 Wins**', inline=False)
    winembed.add_field(name='<:silver:901409597837967360> :flag_de: Micheal Schumacher',value='<:line:903128366054510602><:arr:902911455664414760> **91 Wins**', inline=False)
    winembed.add_field(name='<:bronze:901409640808611850> :flag_de: Sebastian Vettal',value='<:line:903128366054510602><:arr:902911455664414760> **52 Wins**', inline=False)
    winembed.add_field(name='4️⃣ :flag_fr: Alain Prost',value='<:line:903128366054510602><:arr:902911455664414760> **51 Wins**', inline=False)
    winembed.add_field(name='5️⃣ :flag_br: Ayrton Senna',value='<:line:903128366054510602><:arr:902911455664414760> **41 Wins**', inline=False)
    winembed.add_field(name='6️⃣ :flag_es: Fernando Alonso',value='<:line:903128366054510602><:arr:902911455664414760> **32 Wins**', inline=False)
    winembed.add_field(name='7️⃣ :flag_br: Nigel Mansell',value='<:line:903128366054510602><:arr:902911455664414760> **31 Wins**', inline=False)
    winembed.add_field(name='8️⃣ :flag_br: Jackie Stewart',value='<:line:903128366054510602><:arr:902911455664414760> **27 Wins**', inline=False)
    winembed.add_field(name='9️⃣ :flag_br: Jim Clark',value='<:line:903128366054510602><:arr:902911455664414760> **25 Wins**', inline=False)
    winembed.add_field(name='🔟 :flag_at: Niki Lauda',value='<:line:903128366054510602><:arr:902911455664414760> **25 Wins**', inline=False)
    await ctx.send(embed=winembed)

@most_subcommand.command(name='poles', aliases=['pole'])
async def pole_subcommand(ctx):
    poleembed=discord.Embed(title='Most Poles in Formula 1', description='The list of the drivers with most Poles (First in Qualifying)')
    poleembed.add_field(name='<:gold:901409567810940938> :flag_gb: Lewis Hamilton',value='<:line:903128366054510602><:arr:902911455664414760> **101 Poles**', inline=False)
    poleembed.add_field(name='<:silver:901409597837967360> :flag_de: Micheal Schumacher',value='<:line:903128366054510602><:arr:902911455664414760> **68 Poles**', inline=False)




#############################################################################################################




#############################################################################################################
'''Roll command'''

@client.command()
async def roll(ctx, int:None):
    if int == None:
        int = 100
        roll=random.randint(1,int)
        await ctx.send(f'{ctx.author} rolls **{roll}** (1-{int})')



#############################################################################################################
'''Button Calculator'''



#############################################################################################################
#############################################################################################################
'''Reminder command'''

@client.command(case_insensitive = True, aliases = ["remind", "remindme", "rm"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder=None):
    user = ctx.message.author
    embed = discord.Embed(title='Sonique', description='If you have any queries, suggestions or bug reports, please join our Support Server: `?invite`', color=0x55a7f7, timestamp=datetime.datetime.utcnow())
    seconds = 0
    if reminder is None:
        reminder='Nothing'
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        await ctx.send('<:error:899992500150865980> Please specify a proper duration for a reminder!')
    elif seconds < 5:
        await ctx.send('<:error:899992500150865980> You have specified a too short duration! Minimum duration is 5 Seconds.')
    elif seconds > 7776000:
        await ctx.send('<:error:899992500150865980> You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        await ctx.send(f'Alright **{ctx.author.display_name}**, I will remind you about "{reminder}" in **{counter}**.')
        await asyncio.sleep(seconds)
        reminderembed=discord.Embed(title=f'Reminder for {ctx.author}', description=f'Heyo, You asked to be reminded about **"{reminder}"** **{counter}** ago.', color=ctx.author.color)
        reminderembed.add_field(name='Original Message', value=f'[Jump to the Message](https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id})')
        await ctx.author.send(embed=reminderembed)
        return
    await ctx.send(embed=embed)

@reminder.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:error:899992500150865980> You need to specify a duration for the reminder")


#############################################################################################################
'''Snipe and Esnipe Command'''

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(description = snipe_message_content[channel.id])
        em.set_author(name=f'{snipe_message_author[channel.id]}', icon_url=snipe_message_author[channel.id].avatar_url)
        em.set_footer(text = f'Sniped by {ctx.author}')
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in <#{ctx.channel.id}>")


@client.command()
async def esnipe(ctx):
    async def on_message_edit(self, before, after):
        esnipeemb=discord.Embed()
        esnipeemb.add_field(name="Before", value=f'{before.content}')
        esnipeemb.add_field(name="After",vale=f'{after.content}')
        esnipeemb.set_footer(text = f'Sniped by {ctx.author}')
        esnipeemb.set_author(name=f'{snipe_message_author[channel.id]}', icon_url=snipe_message_author[channel.id].avatar_url)
        await ctx.send(embed=esnipeemb)


@client.command()
async def test(ctx):
    bot_msg = await ctx.send('Alright is it one or two')

    try:
        message = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=3.0)
    
    except asyncio.TimeoutError:
        await bot_msg.edit('ouch.')

    else:
        if message.content == 'one':
            await ctx.send('okie 1 one ')
        elif message.content == 'two':
            await ctx.send("okie 2 two")
        else:
            await ctx.send(f'i dont see "{message.content}" in the options -_-')


@client.command()
async def guess(ctx):
    numb=random.randint(1,10)
    bot_msg= await ctx.send('Ok, guess a number between 0-10!')
    numb_ans="0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    try:
        message = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=10.0)
    except asyncio.TimeoutError:
        await bot_msg.reply('You ran outta time sigh')

    else:
        if message.content == numb:
            await message.reply('Thats right!')
        
        else:
            await ctx.send(f'Ahh better luck next time, the number was {numb}')

'''elif message.content != numb_ans:
            await ctx.send(f'I don\'t recall "{message}" present between 0 to 10 -_-')'''
@client.command()
async def suggest(ctx, *,suggestion):
    sugembed=discord.Embed(title=f'Suggestion for {ctx.guild.name}!',description=f'{suggestion}', color=ctx.author.color)
    sugembed.set_author(name=f'{ctx.author}', icon_url={ctx.author.avatar_url})


    

#############################################################################################################
'''Lock and Unlock channel command'''

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'<#{channel.id}> has been locked') 

@lock.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('<:error:899992500150865980> You do not have permissions to use this command')


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'<#{channel.id}> has been unlocked')  

@unlock.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('<:error:899992500150865980> You do not have permissions to use this command')



#############################################################################################################
'''Invite Command'''

@client.command(aliases = ['inv'])
async def invite(ctx):
 embedd = discord.Embed(title=f"Invite {client.user.name}!", color=0xff0000, description=f"Wanna invite {client.user.name}, then [click here](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot)")
 embedd.add_field(name='Have Questions or Suggestions?', value='Join our [Support Server!](https://discord.gg/upDSQFMeNc)')    

 await buttons.send(
		content =None,
		embed = embedd,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Invite",
					url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
				),
			
                Button(
                    style= ButtonType().Link,
                    label='Support Server',
                    url="https://discord.gg/upDSQFMeNc"
                )
            ])
		]
	)


#############################################################################################################
'''AFK command, mention response, remove on message (fix when)'''

@client.command()
async def afk(ctx, mins):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} has gone afk for {mins} minutes.")
    await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break



#############################################################################################################
'''Giveaway'''

@client.command()
@commands.has_permissions(send_messages=True)
async def gstart(ctx, time=None, *, prize=None):
    if time==None:
        return await ctx.send("<:error:899992500150865980> Please include a time for the giveaway!")

    elif prize==None:
        return await ctx.send("<:error:899992500150865980> Please include a prize to giveaway!")
    gembed = discord.Embed(title = f"{prize}!", color=ctx.author.color)
    time_convert = {"s": 1, "m":60, "h":3600, "d":86400}
    gawtime = int(time[0]) * time_convert[time[-1]]
    gembed.add_field(name="React with 🎉 to enter", value=f'Time: **{time}** \n Hosted by: {ctx.author.mention}')
    gembed.set_footer(text=f'Giveaway ends in {time}')
    my_msg = await ctx.send(embed=gembed)


    await my_msg.add_reaction("🎉")
    await asyncio.sleep(gawtime)

    new_gaw_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_gaw_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congrats {winner.mention} on winning **{prize}**! {await ctx.channel.message.link(my_msg)}") 


#############################################################################################################


@client.command()
@commands.is_owner()
async def servers(ctx):
    for guild in client.guilds:
        await ctx.send(f"Server Name: {guild.name} | ID: {guild.id}\nServer Owner: {guild.owner} | ID: {guild.owner.id}")



#############################################################################################################
'''On Ready'''

'''Loading all the Cogs'''

'''Test Cog'''
for file in os.listdir("./Cogs/test"):
    if file.endswith(".py"): 
        name = file[:-3] 
        client.load_extension(f"Cogs.test.{name}")

'''Help Cog'''
for file in os.listdir("./Cogs/Help"):
    if file.endswith(".py"): 
        name = file[:-3] 
        client.load_extension(f"Cogs.Help.{name}")

'''Fun Cogs'''
for file in os.listdir("./Cogs/Fun"):
    if file.endswith(".py"):
        name = file[:-3] 
        client.load_extension(f"Cogs.Fun.{name}")

'''Misc Cogs'''
for file in os.listdir("./Cogs/Misc"):
    if file.endswith(".py"):
        name = file[:-3] 
        client.load_extension(f"Cogs.Misc.{name}")

'''Mod Cogs'''
for file in os.listdir("./Cogs/Mod"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"Cogs.Mod.{name}")

'''Support Server Cogs'''
for file in os.listdir("./Cogs/SupServer"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"Cogs.SupServer.{name}")


############################################################################

@client.event
async def on_ready():
    print('Bot is ready!')
    client.load_extension('dismusic')
    DiscordComponents(client)

############################################################################
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, dismusic.errors.NotConnectedToVoice):
        await ctx.send('You are not connected to any voice channel.')
    if isinstance(error, dismusic.errors.MustBeSameChannel):
        await ctx.send("Please join the channel where the bot is connected to use the music commands!")

#############################################################################################################
'''status, changing status, task..'''

async def ch_pr():
    await client.wait_until_ready()

    statuses = [f'in {len(client.guilds)} servers! | ?help', '?help']
    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(20)




def setup(bot):
  bot.add_cog(Groups(bot))

client.loop.create_task(ch_pr())

#############################################################################################################
'''running'''

client.run("ODg3NjczMTg1NjUzMzcwODgw.YUHkEw.pDRQa8B7jlmwomoVbqmHSbK-mJg") 