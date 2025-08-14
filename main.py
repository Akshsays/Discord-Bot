import discord
# import discord .ext and app_commands for creating commands
from discord.ext import commands
from discord import app_commands
import os # For env
from dotenv import load_dotenv
import datetime
# from numpy import *
# import numexpr

load_dotenv(".env") 
TOKEN = os.getenv("TOKEN")

class client(commands.Bot): #using commands.Bot for slash commands
    async def on_ready(self):
        print(F'logged on as{self.user}!')
        # forcing to the bot to sync the messages
        try:
            synced = await self.tree.sync(guild=discord.Object(id=1391791251031851110))
            print(f"Synced {len(synced)} commands to the server {GUILD_ID}.")

        except Exception as e:
            print(f"Error syncing commands: {e}")

# Message Events            

   # React to a message     
    async def on_message(self,message,member:discord.Member):
        # print(f"Message from: {message.author}:{message.content}") 
        if message.content == "Syst":
            await message.channel.send("He is noob!!")

    # Send message on message edit
    async def on_message_edit(self,before,after):
        if before.content!=after.content:
            await after.channel.send(f"{before.author} Edited there message:\n **Original:** {before.content}\n **Edited** {after.content}\n")               

    # Message on deleting
    async def on_message_delete(self,message):
        if message.author==self.user:
            return
        else:
            await message.channel.send(f'I saw that {message.author}!!')

# Reaction events

    # Message on reaction       
    async def on_reaction_add(self,reaction,user):
        if str(reaction.emoji) == "👍": 
            await reaction.message.channel.send(f'You reacted with this emoji :{reaction.emoji}!!')

    # Send message on removing reaction
    async def on_reaction_remove(self,reaction,user):
        await reaction.message.channel.send("Why did you removed the reaction 🥀")

# User join and leave events

    # Welcome user when joined the server with and embed
    async def on_member_join(self,member):
        channel = self.get_channel(1398593475250749450)
        embed=discord.Embed(title=f"📸 Lights, camera, action!",description=f"Welcome to **Basement** \n\n Get ready to supercharge your Discord server with our feature-rich bot. Join lively discussions, get help with ABOT, and connect with a friendly bunch of enthusiasts. Were excited to have you here.")
        if channel:
            await channel.send(f'{member.mention} landed here')
            await channel.send(embed=embed)

    # Send message on user leaves
    async def on_member_remove(self,member):
        channel=self.get_channel(1398594677065650206)
        if channel:
            await channel.send(f'{member.name} Left us 🥀')

    # async def on_member_banned(self,member):
    #     channel=self.get_channel(1398574226297982987)
    #     if channel:
    #         await channel.send(f"Bohaha {member.name} got banned")

# Small automod            
    
    # bad language
    async def on_message(self,message):
            badwords=["fuck","dick","mf","shit"]
            mesg_content=message.content.lower()
            if any(word in mesg_content for word in badwords):
                await message.delete()
                await message.channel.send(f"Hey {message.author} please don't use such language")
    

GUILD_ID = discord.Object(id=1391791251031851110) # for insuring that the bot run in the specific server only

intents=discord.Intents.all() 
intents.message_content= True
intents.members=True                
client=client(command_prefix="!",intents=intents)   


# Basic embed desgin
@client.tree.command(name="embed",description="basic embed with title,description,field and footer",guild=discord.Object(id=1391791251031851110))
async def embed(interaction:discord.Interaction,title:str,description:str,channel:discord.TextChannel):
    embed=discord.Embed(title=title,description=description,color=discord.Color.red())
    # embed.set_footer(text="This is a footer")
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message(f"{interaction.user} Sorry you can use this command",ephemeral=True)
        return
    else:
        await channel.send(embed=embed) # Send directly to selected channel
        await interaction.response.send_message(f"Embed sent to {channel.mention}",ephemeral=True)

# Button response and style
class View(discord.ui.View): 
    @discord.ui.button(label="Click me",style=discord.ButtonStyle.red,emoji="🙃")
    async def button_callback(self,button,interaction):
        await button.response.send_message("You clicked the button",ephemeral=True)

    #second button   
    @discord.ui.button(label="Second button",style=discord.ButtonStyle.grey,emoji="🥀")
    async def secondb_callback(self,button,interaction): # should give different function name for each button
        await button.response.send_message("This was the second button",ephemeral=True)

#Buttons send on slash cmd
@client.tree.command(name="button",description="add a button",guild=discord.Object(id=1391791251031851110))
async def buttons(interaction:discord.Interaction):
    await interaction.response.send_message(view=View())

# Mod Commands

# Kick user with an embed
@client.tree.command(name="kick",description="kick User",guild=discord.Object(id=1391791251031851110))
@app_commands.describe(user="The user to kick", reason="The reason for kicking")
async def kickembed(interaction:discord.Interaction,user:discord.Member,reason:str):
    embed2=discord.Embed(title="Kicked User",description="kicked the user from the server",color=discord.Color.red())
    embed2.add_field(name=f"User:{user.name}",value=f"Reason:{reason}",inline=False)
    embed2.set_image(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXNwdGZlcDNpcDNwNng1b2QxN3A2bjh4eG8wNmRhM241Mzl1c3N5cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UfkfLErH5QMlzXChcF/giphy.gif")
    # Permission check
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ You don't have permission to kick members.", ephemeral=True)
        return
    else:
            channel=interaction.guild.get_channel(1398574226297982987)
            dm=client.get_user(user)
            await user.send(f"You have been kicked from the server due to the reason: {reason}")
            await user.kick(reason=reason)
    if channel:
            await channel.send(embed=embed2)
            await interaction.response.send_message(f"User Sucessfully kicked",ephemeral=True)

# Ban User
@client.tree.command(name="ban",description="Ban user",guild=discord.Object(id=1391791251031851110))
async def ban(interaction:discord.Interaction,user:discord.Member,reason:str):
    # check permission
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You don't have require permission to use this command",ephemeral=True)
        return
    else:
        dm=client.get_user(user)
        await user.send(f"You have been banned from the server due to: {reason}")
        await user.ban(reason=reason)
        await interaction.response.send_message(f"{user} is been banned from the server",ephemeral=True)

# Unban user
@client.tree.command(name="unban",description="Unban user",guild=discord.Object(id=1391791251031851110))
async def ban(interaction:discord.Interaction,user_id:discord.User,reason:str):
    await client.fetch_user(user_id)
    # check permission
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You don't have require permission to use this command",ephemeral=True)
        return
    else:
        await interaction.guild.unban(user_id,reason=reason)
        await interaction.response.send_message("Unbanned from the server",ephemeral=True)
  
# Timeout user in minutes
@client.tree.command(name="timeout",description="Timeout user",guild=discord.Object(id=1391791251031851110))
async def timeout(interaction:discord.Interaction,user:discord.Member,duration:int,reason:str):
    if not interaction.user.guild_permissions.mute_members:
        await interaction.response.send_message("You don't have required permission to use this command",ephemeral=True)
        return 
    else:
        until_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=duration)
        await user.timeout(until_time,reason=reason)
        await interaction.response.send_message(f"{user.mention} Has been muted till {duration} minute")
 
 # Remove user timeout
@client.tree.command(name="unmute",description="Remove user timeout",guild=discord.Object(id=1391791251031851110))
async def unmute(interaction:discord.Interaction,user:discord.Member,reason:str):
    if not interaction.user.guild_permissions.mute_members:
        await interaction.response.send_message(f"{interaction.user.mention} You don't have required permission to use this command",ephemeral=True)
        return
    else:
        await user.timeout(None,reason=reason)
        await interaction.response.send_message(f"{user.mention} Has been unmuted")
        
# Report command
@client.tree.command(name="report",description="Report the user",guild=discord.Object(id=1391791251031851110))
@app_commands.describe(message="enter the message to be reported",user="Enter user to report",reason="Enter the reason of report",comment="Add extra info")
async def report(interaction:discord.Interaction,user:discord.Member,message:str,reason:str,comment:str):
    rpembed=discord.Embed(title="Report",description=f"{interaction.user.mention} reported {user} for {reason}",color=discord.Color.red())
    rpembed.add_field(name="Message / Evidence", value=message, inline=False)
    rpembed.add_field(name="Comment", value=comment, inline=False)

    channelid=1404893284890837013
    targetchannel=client.get_channel(channelid)
    if targetchannel:
        await targetchannel.send(embed=rpembed)
    await interaction.response.send_message(f"{interaction.user} Thanks for reporting the user!!",ephemeral=True)

# bits to bytes converter cmd
@client.tree.command(name="find",description="Calculate bits and bytes",guild=discord.Object(id=1391791251031851110))
async def byt(interaction:discord.Interaction,bits:float,bytes:float):
    b1=bits/8
    b2=bytes*8
    await interaction.response.send_message(f"The given number of bits {bits} are equal to {b1} number of bytes",ephemeral=True)
    await interaction.followup.send(f"The given number of byes {bytes} are equal to {b2} number of bits",ephemeral=True)

# Bot ping
@client.tree.command(name="ping",description="Tells the ping of the bot",guild=discord.Object(id=1391791251031851110))
async def pong(interaction:discord.Interaction):
    latency=round(client.latency*8)
    await interaction.response.send_message(f"Bot ping: {latency}",ephemeral=True)

client.run(TOKEN)
