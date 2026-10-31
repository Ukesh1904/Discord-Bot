import discord
from discord.ext import commands
import datetime
import os
import asyncio

class moderation(commands.Cog):
    def __init__(self, bot):
        self_client = bot

    @commands.Cog.listener()
    async def on_ready():
        print("Ban command is ready to use.")
        
    # Code for ban    
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None): 
        # Check if the command invoker has permissions to kick members
        if ctx.author.guild_permissions.ban_members:
            if ctx.guild.me.guild_permissions.ban_members:
                try:
                    await member.ban(reason=reason)
                    await ctx.send(f'**{member.name}** has been banned.')
                except discord.Forbidden:
                    await ctx.send("The bot doesn't have permission to ban members.")
                except discord.HTTPException:
                    await ctx.send("An error occurred while trying to ban the member.")
            else:
                await ctx.send("The bot doesn't have permission to ban members.")
        else:
            await ctx.send("You don't have permission to ban a member.")
            
    # Command to unban a user
    @commands.command()
    async def unban(self, ctx, *, member):
        if ctx.author.guild_permissions.administartion:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')
                    return
        else:
            await ctx.send("You do not have permission to use this command.")


    # # Command to kick a user
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        # Check if the command invoker has permissions to kick members
        if ctx.author.guild_permissions.kick_members:
            if ctx.guild.me.guild_permissions.kick_members:
                try:
                    await member.kick(reason=reason)
                    await ctx.send(f'**{member.name}** has been kicked.')
                except discord.Forbidden:
                    await ctx.send("The bot doesn't have permission to kick members.")
                except discord.HTTPException:
                    await ctx.send("An error occurred while trying to kick the member.")
            else:
                await ctx.send("The bot doesn't have permission to kick members.")
        else:
            await ctx.send("You don't have permission to kick a member.")



    # Command to timeout a user 
    @commands.command(aliases = ["to","TO"])
    async def timeout(self, ctx, member: discord.Member = None , timelimit= None):
        if ctx.author.guild_permissions.administrator:
                if member is None:
                    await ctx.send("Please specify a member to timeout.")
                    return
                
                if member == ctx.author:
                    await ctx.send("You cannot timeout yourself.")
                    return
                
                if timelimit == None:
                    await ctx.send("Enter s certain time period.")
                    return 
                try:
                    if "s" in timelimit:
                        gettime = timelimit.strip("s")
                        newtime = datetime.timedelta(seconds=int(gettime))
                        await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
                        await ctx.send(f"**{member.name}** has been timeouted for {gettime} seconds by **{ctx.author}**.")
                    elif "m" in timelimit:
                        gettime = timelimit.strip("m")
                        newtime = datetime.timedelta(minutes=int(gettime))
                        await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
                        await ctx.send(f"**{member.name}** has been timeouted for {gettime} minutes by **{ctx.author}**.")
                    elif "d" in timelimit:
                        gettime = timelimit.strip("d")
                        newtime = datetime.timedelta(days=int(gettime))
                        await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
                        await ctx.send(f"**{member.name}** has been timeouted for {gettime} days by **{ctx.author}**.")
                except discord.Forbidden:
                    await ctx.send("The bot doesn't have permission to timeout member.")
        elif not ctx.author.guild_permissions.administrator:
            await ctx.send("You don't have permission to use this command.")
            
    #code to remove timeout from a user       
    @commands.command(aliases =["rto","RTO"])
    async def remove_timeout(self, ctx, member: discord.Member = None):
        if ctx.author.guild_permissions.administrator:
            if member is None:
                await ctx.send("Please specify a member to remove timeout.")
                return
                
            if member == ctx.author:
                await ctx.send("You cannot remove timeout for yourself.")
                return
                
            if member.timed_out_until is None:
                await ctx.send(f"{member.mention} is not currently timed out.")
                return
                
            await member.edit(timed_out_until=None)
            await ctx.send(f"The timeout for {member.mention} has been removed.")
        elif not ctx.author.guild_permissions.administrator:
            await ctx.send("You have no permission to remove timeout.")
            
    # Command to delete a specified number of messages
    @commands.command(aliases = ["purge"])
    async def clear(self, ctx, amount: int):
        if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=amount+1)
            message = await ctx.send(f"{amount} message has been deleted.")
            await asyncio.sleep(3)
            await message.delete()
        else:
            await ctx.send("You do not have permission to use this command.")
            
            
    # Command to delete certain word from the chat 
    @commands.command()
    async def delete(self, ctx, word: str):
        if ctx.author.guild_permissions.administrator:
            if word in ctx.message.content:
                messages = []
                async for message in ctx.channel.history(limit=100):
                    messages.append(message)
                for message in messages:
                    if word in message.content:
                        await message.delete()
                confirmation_message = await ctx.send(f"All messages containing **__{word}__** have been deleted.")
                await asyncio.sleep(2)
                await confirmation_message.delete()
            else:
                await ctx.send("Message containing word **__{word}__** was not  found.")
            
async def setup(bot):
    await bot.add_cog(moderation(bot))