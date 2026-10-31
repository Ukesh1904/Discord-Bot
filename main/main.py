import discord
from discord.ext import commands
from discord import app_commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions 
import os 
import asyncio
import requests
import json
import random
import datetime


bot = commands.Bot(command_prefix = '-', intents=discord.Intents.all())

# insert TOKEN created from Discord Developer Portal
TOKEN = ""

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + "\t -" + json_data[0]["a"]
    return(quote)

def get_joke():
    response2 = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response2.json()
    setup = data['setup']
    punchline = data['punchline']
    joke = f"{setup}\n||{punchline}||"
    return joke


bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("The bot is now ready to use.")
    print("----------------------------")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.strip().startswith(":quote"):
        quote = get_quote()
        embed_msg = discord.Embed(description=quote, color=discord.Color.random())
        await message.channel.send(embed=embed_msg)

    elif message.content.strip().startswith(":joke"):
        joke = get_joke()
        k_msg = discord.Embed(description=joke, colour= discord.Color.random())
        await message.channel.send(embed=k_msg)
    
    # RPS game
    
    rps_game = [
        "Rock",
        "Paper",
        "Scissor"
    ]
    
    rps_roll = random.choice(list(rps_game))
    
    if message.content.strip().startswith("-rps rock"):
            
        if rps_roll == "Rock":
            await message.channel.send(f"I choose {rps_roll}. We tied.")
        elif rps_roll == "Paper":
            await message.channel.send(f"I choose {rps_roll}. I won.")
        elif rps_roll == "Scissor":
            await message.channel.send(f"I choose {rps_roll}. I loose.")

    elif message.content.strip().startswith("-rps paper"):
        if rps_roll == "Paper":
            await message.channel.send(f"I choose {rps_roll}. We tied.")
        elif rps_roll == "Scissor":
            await message.channel.send(f"I choose {rps_roll}. I won.")
        elif rps_roll == "Rock":
            await message.channel.send(f"I choose {rps_roll}. I loose.")
                
    elif message.content.strip().startswith("-rps scissor"):
        if rps_roll == "Scissor":
            await message.channel.send(f"I choose {rps_roll}. We tied.")
        elif rps_roll == "Paper":
            await message.channel.send(f"I choose {rps_roll}. I loose.")
        elif rps_roll == "Rock":
            await message.channel.send(f"I choose {rps_roll}. I won.")
            
    elif message.content.strip().startswith("-rps"):
        await message.channel.send("Choose any one: rock, paper or scissor.\neg:- :rps rock")
       
    # Coinflip game 
    coin = [
        "Head",
        "Tail"
    ]
    
    cf = random.choice(list(coin))
    
    if message.content.strip().startswith("-cf head"):
        if cf == "Head":
            await message.channel.send(f"The coin flipped on {cf}. You have won.")
        else:
            await message.channel.send(f"The coin flipped on {cf}. You have lost.")

    elif message.content.strip().startswith("-cf tail"):
        if cf == "Tail":
            await message.channel.send(f"The coin flipped on {cf}.You have won.")
        else:
            await message.channel.send(f"The coin flipped on {cf}.You have lost")
            
    elif message.content.strip().startswith("-cf"):
            await message.channel.send(f"Choose any one : head or tail.\neg:- :cf head")
            
    else:
        await bot.process_commands(message)
    
    

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention} ")
    
    
@bot.event
async def on_member_join(member):
    welcome_message = f"Hey {member.mention},Welcome to **{member.guild.name}** server! We're glad to have you here.I hope you will enjoy your stay in this server."
    try:
        await member.send(welcome_message)
    except discord.Forbidden:
        # If the user has DMs disabled or the bot cannot send DMs to the user
        print(f"Failed to send a welcome message to {member.name}.")
        



# Code for help command         
@bot.command()
async def help(ctx):
    help_embed = discord.Embed(title="Help commands", description="All commands info are given below.", color=discord.Color.random())

    help_embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    help_embed.add_field(name="ban/unban", value="Ban/unban a user from the server.", inline= False)
    help_embed.add_field(name="kick", value="Kick a user from the server.", inline= False)
    help_embed.add_field(name="timeout/to/remove_timeout(rto)", value="Timeout/Remove timeout a user from the server.", inline= False)
    help_embed.add_field(name="userinfo/ui/uinfo", value="Provides a information of the user.", inline= False)
    help_embed.add_field(name="guildinfo/gi/serverinfo/si", value="Information of the server.", inline= False)
    help_embed.add_field(name="roles",value="Shows all the roles of the server.",inline=False)
    help_embed.add_field(name="boosters/sb/SB",value="Shows the boosts, boost level and boosters of the server.",inline=False)
    help_embed.add_field(name="membercount/mc", value="Show the server member count.", inline= False)
    help_embed.add_field(name="quote", value="Send random quotes.", inline= False)
    help_embed.add_field(name="joke",value="Send random joke.",inline=False)
    help_embed.add_field(name="botinfo/bi",value="Shows bot info.",inline= False)
    help_embed.add_field(name="purge/clear",value="Delete certain number of messgaes.",inline=False)
    help_embed.add_field(name="delete",value="Delete a specific word from the chat.",inline=False)
    help_embed.add_field(name="rps",value="It's a rock, paper and scissor game which u play with bot.",inline=False)
    help_embed.add_field(name="cf",value="Its a coinflip game.",inline=False)
    help_embed.set_footer(text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar)

    await ctx.send(embed=help_embed)
    



# Code for bot info     
@bot.command(aliases = ["bi"])
async def botinfo(ctx):
        embed = discord.Embed(title="Bot Information", color=discord.Color.blue())
        embed.set_thumbnail(url=bot.user.avatar)
        embed.add_field(name="Bot Name", value=bot.user.name, inline=True)
        embed.add_field(name="Bot ID", value=bot.user.id, inline=True)
        embed.add_field(name=" ",value=" ",inline=False)
        embed.add_field(name="Created at",value=bot.user.created_at.strftime("%Y-%m-%d | %H:%M:%S"), inline=True)
        app_info = await bot.application_info()
        embed.add_field(name="Created by ", value=app_info.owner.mention, inline=True)
        await ctx.send(embed=embed)

            

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())