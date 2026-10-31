import discord
from discord.ext import commands
import random 
import os
import asyncio

td = commands.Bot(command_prefix = "o", intents = discord.Intents.all())


token = ""


td.remove_command("help")


choose = {
    "Truth",
    "Dare"
}

truth_qns = {
    "What is the most embarrassing thing you've done in public?",
    "Who is your crush ?",
    "What's your secret that you've never told anyone?",
    "Have you ever peed in the bed?",
    "What's the silliest thing you've ever done to impress someone?",
    "What's the weirdest food combination you've ever tried and liked?",
    "Have you ever pretended to know a song or movie just to fit in?",
    "Have you ever laughed at a joke that you didn't understand just to seem polite?",
    "What's the most embarrassing nickname you've ever had?",
    "Have you ever tripped and fallen in public? If so, how did you recover?",
    "What's the most embarrassing thing you've done in front of a crush?"
}

dare_task = {
    "Send a message in a public Discord server saying __'discod user kingken10 is gay.'__ without any context.",
    "Sing a silly song in the voice chat.",
    "Write a short poem about your favorite snack and share it in the every server you are in.",
    "Send a dancing video of yourself.",
    "To propose to discord user = kingken10.",
    "Speak in a funny accent for the next 10 minutes.",
    "Change your Discord status to __'discod user kingken10 is gay.'__ for the next hour.",
    "Send a message in the server asking if anyone wants to join your imaginary furry club.",
    "Make up a funny joke and share it in the server's general chat."
}

@td.event
async def on_ready():
    print("Now you can play Truth and Dare with your friends.")
    print("--------------------------------------------------")


@td.command()
async def roll(ctx):
    rd = random.choice(list(choose))

    if rd == "Truth" :
        qns = random.choice(list(truth_qns))
        await ctx.send(f"You got truth.\nYour question is : **{qns}**")
    else:
        task = random.choice(list(dare_task))
        await ctx.send(f"You got dare.\nYour task is : **{task}**")


@td.command()
async def help(ctx):
    msg = discord.Embed(title="Bot Command", color = discord.Color.random())
    msg.add_field(name="roll", value="It will roll truth or dare and gives a qns or task to do.",inline= False)

    await ctx.send(embed=msg)   

# @td.command()
# async def coinflip(ctx, choice=None):
#     coin = ['Head' or 'head', 'Tail' or 'tail']
#     if choice not in coin:
#         await ctx.send("Invalid choice. Please choose between 'Head' and 'Tail'.")
#     else:
#         result = random.choice(coin)
#         if choice == result:
#             await ctx.send(f"The coin flips on {result}. You win!")
#         else:
#             await ctx.send(f"The coin flips on {result}. You lose!")

# async def load():
#     for filename in os.listdir("./cog2"):
#         if filename.endswith(".py"):
#             await td.load_extension(f"cog2.{filename[:-3]}")

# async def main():
#     async with td:
#         await load()
#         await td.start(token)

# asyncio.run(main())

td.run(token)