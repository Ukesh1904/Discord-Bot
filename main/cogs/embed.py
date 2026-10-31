import discord
from discord.ext import commands
import datetime
import os
import asyncio

class embed(commands.Cog):
    def __init__(self, bot):
        self_client = bot

    @commands.Cog.listener()
    async def on_ready():
        print("Embed command is ready to use.")
        
    @commands.command()
    async def rule(self, ctx):
        if ctx.author.guild_permissions.administrator:
            embeded_msg = discord.Embed(title="Rules", description="1. **Respect and Be Civil:**\n   - Treat all members with respect.\n   - Avoid hate speech, discrimination, and harassment.\n   - Refrain from personal attacks or insults.\n\n2. **No Spamming:**\n   - Avoid excessive, repetitive, or irrelevant messages.\n   - No excessive use of emojis or capital letters.\n\n3. **No NSFW Content:**\n   - Prohibit explicit, adult, or not-safe-for-work content.\n\n4. **No Self-Promotion:**\n   - Limit self-promotion and advertising. Create a dedicated channel for this if needed.\n\n5. **Stay On-Topic:**\n   - Keep discussions relevant to the designated channels.\n\n6. **No Doxxing or Personal Information:**\n   - Do not share personal information about yourself or others.\n\n7. **Respect Privacy:**\n   - Do not share other\'s private messages without their consent.\n\n8. **No Trolling or Baiting:**\n   - Do not post content intended to provoke or upset others.\n\n9. **Use Appropriate Language:**\n   - Avoid excessive profanity or inappropriate language.\n\n10. **Moderation and Enforcement:**\n   - Outline consequences for rule violations, which may include warnings, temporary mutes, or bans.\n\n11. **Reporting:**\n   - Encourage members to report rule violations to the moderators.\n\n12. **Community Feedback:**\n   - Allow members to suggest changes or provide feedback on the server\'s rules and setup.", color=discord.Color.purple())
            embeded_msg.set_thumbnail(url=ctx.guild.icon)
            # embeded_msg.add_field(name="Name of field",value="Value of field", inline=False)
            embeded_msg.set_image(url="https://media1.tenor.com/m/vIKSPoL_ycUAAAAC/discord-rules.gif")
            embeded_msg.set_footer(text="Members are requested to follow the rules of the server.",icon_url=ctx.guild.icon)
            await ctx.send(embed=embeded_msg)
        else:
            await ctx.send("You do not have permission to use this command.")
        

    @commands.command(aliases = ["ri"])
    async def roleinfo(self, ctx):
        if ctx.author.guild_permissions.administrator:
            ri_msg = discord.Embed(title="Role Info",description="<@&1223639811911454791> <a:arrows:1243537651974410282> Owner\n\n<@&1223171024426635286> <a:arrows:1243537651974410282> Co-owner\n\n<@&1223280849550704731> <a:arrows:1243537651974410282> Head Admin\n\n<@&1223281080761585704> <a:arrows:1243537651974410282> Admin\n\n<@&1223261119909728306> <a:arrows:1243537651974410282> Head Mod\n\n<@&1223281262463291502> <a:arrows:1243537651974410282> Mod\n\n<@&1226365163049848852> <a:arrows:1243537651974410282> Server boosters\n\n<@&1224289377316900895> <a:arrows:1243537651974410282> Role for account donator\n\n<@&1223487488614596698> <a:arrows:1243537651974410282> Partnership Manager\n\n<@&1223220243779031042> <a:arrows:1243537651974410282> Members role\n\n<@&1223253384837206117> <a:arrows:1243537651974410282> Server bots\n\n\n# MM Role:\n<@&1223287881133592686> <a:arrows:1243537651974410282> You must 100+ have vouches.\n\n<@&1223287921113825422> <a:arrows:1243537651974410282> Approved by higher staff\n\n<@&1223287954710204446> <a:arrows:1243537651974410282> Approved by higher staff or by owner\n\n\n# Roles for members :\n\nLevel 10 <a:arrows:1243537651974410282> <@&1254034068581122111>\n\nLevel 20 <a:arrows:1243537651974410282> <@&1254034100709490708>\n\nLevel 30 <a:arrows:1243537651974410282> <@&1254034133559283784>\n\nLevel 40 <a:arrows:1243537651974410282> <@&1254034169822973954>\n\nLevel 50 <a:arrows:1243537651974410282> <@&1254034201573855357>\n\n\n> The roles will be provided by owner so if you want to apply for staff and mm role create ticket in <#1223184019647238215>",color=discord.Color.random())
            ri_msg.set_thumbnail(url="https://media1.tenor.com/m/9_Fp55km98gAAAAC/ichigo-bleach.gif")
            await ctx.send(embed=ri_msg)
        else:
            await ctx.send("You do not have permission to use this command.")
        
    @commands.command()
    async def sa(self, ctx):
        if ctx.author.guild_permissions.administrator: 
            embed_msg = discord.Embed(title="Staff Application",description="Create ticket if you want to be staff and become mm in this server.\n\nRead <#1254034934369222716> for mm and for staff you can get upto head mod.\n\nPlease do not create unnecessary ticket.\n\nThank You!!🌹",color=discord.Color.random())
        #  embed_msg.set_thumbnail(url=ctx.guild.icon)
            await ctx.send(embed=embed_msg)
        else:
            await ctx.send("You do not have permission to use this command.")
        
    # USER INFO CODE
    @commands.command(aliases=['ui', 'uinfo']) 
    async def userinfo(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        embed = discord.Embed(title="User Information", color=discord.Color.random())
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
        embed.add_field(name="Roles",value=" ".join([role.mention for role in user.roles]),inline=False)
        key_permissions = {
        'administrator': 'Administrator',
        'manage_guild': 'Manage Server',
        'ban_members': 'Ban Members',
        'kick_members': 'Kick Members',
        'manage_channels': 'Manage Channels',
        'manage_roles': 'Manage Roles',
        'manage_messages': 'Manage Messages'
    }

            # Retrieve and format key permissions
        permissions = user.guild_permissions
        perm_list = [name for perm, name in key_permissions.items() if getattr(permissions, perm)]
        embed.add_field(name="Key Permissions", value=", ".join(perm_list) if perm_list else "None", inline=False)
        # embed.add_field(name="Permission",value=user.guild_permissions,inline=False)
        embed.add_field(name="Bot", value=user.bot, inline=False)
        embed.add_field(name="Created At", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        embed.set_footer(text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar)
        
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.send(embed=embed)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        
        
# SERVE INFO CODE        
    @commands.command(aliases = ['si', 'serverinfo', 'gi'])
    async def guildinfo(self, ctx):
        guild = ctx.guild

        # Create an embed for server info
        embed2 = discord.Embed(title="Server Information", color=discord.Color.random())
        embed2.set_thumbnail(url=guild.icon)
        embed2.add_field(name="Server Name", value=guild.name, inline=True)
        embed2.add_field(name="Server ID", value=guild.id, inline=True)
        embed2.add_field(name="Owner", value=guild.owner.mention, inline=False)
        embed2.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author}.", icon_url= ctx.author.avatar)
        embed2.add_field(name="Members", value=guild.member_count, inline=True)
        role_count = len(guild.roles) - 1
        embed2.add_field(name="Roles", value=role_count, inline=True)
        channel_count = len(guild.channels) - 1 
        embed2.add_field(name="Channels", value=channel_count, inline=True)
        boosts = guild.premium_subscription_count
        embed2.add_field(name="Boosts",value=boosts, inline= False)
        level = 0
        if boosts <= 0:
            level = 0
        elif boosts >= 2:
            level = 1
        elif boosts >= 7:
            level = 2
        elif boosts >= 14:
            level = 3
        embed2.add_field(name="Boost Level",value=level, inline= True)

        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.send(embed=embed2)
        else:
            await ctx.reply(embed=embed2, mention_author=False)
        
        
# COMMAND FOR MEMBER COUNT
    @commands.command(aliases = ["MC",'mc'])
    async def membercount(self, ctx):
        guild = ctx.guild
        
        embed = discord.Embed(title=guild.name, color= discord.Color.random())
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(name="Total members",value=guild.member_count, inline = False)
        bot_count = sum(1 for member in guild.members if member.bot)
        embed.add_field(name="Bots",value=bot_count, inline = False)
        embed.set_footer(text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed)
        
        
# SERVER ROLE LIST         
    @commands.command()
    async def roles(self, ctx):
        roles = ctx.guild.roles
        
        role_name = [role.mention for role in roles]
        role_msg = discord.Embed(title="List of roles:",description=", ".join(role_name), color= discord.Color.random())
        role_msg.set_footer(text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=role_msg)
        
 
# # TO KNOW BOOSTERS       
#     @commands.command(aliases =["SB","sb"])
#     async def boosters(self, ctx):
#         # Get the guild's booster role
#         guild = ctx.guild
        
#         boosts = guild.premium_subscription_count
#         level = 0
#         if boosts == 0:
#             level = 0
#         elif boosts >= 2:
#             level = 1
#         elif boosts >= 7:
#             level = 2
#         elif boosts >= 14:
#             level = 3
        
#         booster_role = discord.utils.get(ctx.guild.roles, name="𝙽𝚘𝚋𝚕𝚎𝚜")
#         if booster_role is None:
#             await ctx.send("No booster role found in this server.")
#             return
        
#         # Find members who have the booster role
#         boosters = [member for member in ctx.guild.members if booster_role in member.roles]
        
#         # If no boosters found
#         if not boosters:
#             await ctx.send("There are no boosters in this server.")
#             return
        
#         # Format booster names
#         booster_names = "\n".join([booster.mention for booster in boosters])
        
#         # Create an embed to display the list of boosters
#         embed = discord.Embed(title="Server Boost Info", color=discord.Color.gold())
#         embed.add_field(name="Boosts",value=boosts,inline = False)
#         embed.add_field(name="Server boost level",value=level,inline= False)
#         embed.add_field(name="Server Boosters",value=booster_names,inline=False)
#         embed.set_footer(text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar)
#         await ctx.send(embed=embed)

    @commands.command(aliases=["SB", "sb"])
    async def boosters(self, ctx):
        # Get the guild's booster role
        guild = ctx.guild
        
        # Check the number of boosts and determine the boost level
        boosts = guild.premium_subscription_count
        level = 0
        if boosts >= 14:
            level = 3
        elif boosts >= 7:
            level = 2
        elif boosts >= 2:
            level = 1
        
        # Automatically find the booster role
        booster_role = None
        for role in guild.roles:
            if role.is_premium_subscriber():
                booster_role = role
                break

        if booster_role is None:
            await ctx.send("No booster role found in this server.")
            return
        
        # Find members who have the booster role
        boosters = [member for member in ctx.guild.members if booster_role in member.roles]
        
        # If no boosters found
        if not boosters:
            await ctx.send("There are no boosters in this server.")
            return
        
        # Format booster names
        booster_names = "\n".join([booster.mention for booster in boosters])
        
        # Create an embed to display the list of boosters
        embed = discord.Embed(title="Server Boost Info", color=discord.Color.gold())
        embed.add_field(name="Boosts", value=boosts, inline=False)
        embed.add_field(name="Server Boost Level", value=level, inline=False)
        embed.add_field(name="Server Boosters", value=booster_names, inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    

# Code for GW rules embed
    @commands.command(aliases = ['gwr'])
    async def GWR(self, ctx):
        GW_embed = discord.Embed(title="GIVEAWAY RULES",description="> - No alt accs\n> - No J4J\n> - Rejoin/Fake/No mutal = Not counting\n> - Acc must be must be +1 month\n> - Acc must be atleast in 4 mutual servers\n> - Check invites only in bot-command channel [Checking invites on chat might lead u to get warn.]\n> - Claim time = 10 sec\n> - Send invites proofs to <@1136726620368023663>.\n\n# For Boosters:\n\n\n> - 1 Boost = Half requirement\n> - 2 Boost = No Requirement\n> - Claim time = 15 sec",color=discord.Color.random())
        
        await ctx.send(embed=GW_embed)
    

        
    @commands.command()
    async def da(self, ctx):
        if ctx.author.guild_permissions.administrator:
            da_msg = discord.Embed(description="> <a:arrow:1239512639369904169> Donate account to <@1136726620368023663> if u want to lower your requirement in GWs.\n> \n> <a:arrow:1239512639369904169> Your requirement will be lower according to the account you provide.\n> \n>  <a:owner:1245786636810453053> Thank you!!", color = discord.Color.random())
            da_msg.set_thumbnail(url="https://media1.tenor.com/m/RuQw_TQ24uwAAAAC/anime.gif")
                
            await ctx.send(embed=da_msg)
        else:
            await ctx.send("You do not have permission to use this command.")
        

    @commands.command()
    async def sr(self, ctx):
        if ctx.author.guild_permissions.administrator:    
            sr = discord.Embed(title="Staff Rule",description="1. Staffs are requested to keep conversations friendly and avoid being rude or disrespectful to the server members or server staff.\n\n2. Any sensitive information shared within staff channels must be kept confidential and not shared outside of authorized staff members.\n\n3. Staff must remain impartial and fair when resolving disputes or addressing issues within the server, avoiding any bias or favoritism. (i.e. Treat all members equally, regardless of their background, status, or opinions. Don't show favoritism or discriminate against anyone.)\n\n4. Staff must not engage in any form of abuse, harassment, or discrimination towards other members. Any such behavior will result in timeout, warn or demote.\n\n5. Staff should only use their moderation powers when necessary and in accordance with the server's guidelines. Abuse of power will not be tolerated.\n\n6. Staff members are encouraged to collaborate and communicate with each other effectively to ensure smooth operation of the server and consistent enforcement of rules.\n\n7. Staff members should be open to constructive feedback from both server management and fellow staff members, and actively work towards improving their performance and contributions to the server.\n\n8. Staff members are requested not to engage in any form of bullying, harassment, or discrimination towards other users. Everyone should feel safe and welcome in the server.\n\n9. Staff having manage role permission are not allowed to give or create role without owner’s permission (does not apply to head admins and above staff).", colour = discord.Color.random())
            sr.set_thumbnail(url="https://media1.tenor.com/m/wDVKM3q-lsIAAAAC/toshiro-hitsugaya.gif")
            await ctx.send(embed=sr)
        else:
            ctx.send("You do not have permission to use this command.")
            
    @commands.command()
    async def pr(self,ctx):
        if ctx.author.guild_permissions.administrator:
            pr = discord.Embed(title="=======PARTNERSHIP RULES=========", description="<@&1147435693728092271> for servers at 1200 and above\n\n**@here** for servers between 500-1000\n\nNo ping for servers below 200 members", color= discord.Color.random())
            # pr.set_thumbnail(url="")
            await ctx.send(embed=pr)
        else:
            ctx.send("You do not have the permission to use this command.")
        
async def setup(bot):
    await bot.add_cog(embed(bot))