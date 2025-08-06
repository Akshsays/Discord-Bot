import discord
# import discord .ext and app_commands for creating commands
from discord.ext import commands
from discord import app_commands
import os # For env
from dotenv import load_dotenv
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

   # React with specific text     
    async def on_message(self,message):
        # print(f"Message from: {message.author}:{message.content}") 
        if message.content == "Syst":
            await message.channel.send("He is noob!!")

    # Message on deleting
    async def on_message_delete(self,message):
        if message.author==self.user:
            return
        else:
            await message.channel.send(f'I saw that {message.author}!!')

    # Message on reaction       
    async def on_reaction_add(self,reaction,user):
        if str(reaction.emoji) == "👍": 
            await reaction.message.channel.send(f'You reacted with this emoji :{reaction.emoji}!!')

    # Send message on removing reaction
    async def on_reaction_remove(self,reaction,user):
        await reaction.message.channel.send("Why did you removed the reaction 🥀")

    # Send message on message edit
    async def on_message_edit(self,before,after):
        if before.content!=after.content:
            await after.channel.send(f"{before.author} Edited there message:\n **Original:** {before.content}\n **Edited** {after.content}\n")   

    # Welcome user when joined the server
    async def on_member_join(self,member):
        channel = self.get_channel(1398593475250749450)
        if channel:
            await channel.send(f'Welcome to the server king {member.mention}')

    # Send message on user remove
    async def on_member_remove(self,member):
        channel=self.get_channel(1398594677065650206)
        if channel:
            await channel.send(f'{member.name} Left us 🥀')
    
    # # bad language
    # async def on_message(self,message):
    #         badwords=["fuck","dick","mf","shit"]
    #         mesg_content=message.content.lower()
    #         if any(word in mesg_content for word in badwords):
    #             await message.delete()
    #             await message.channel.send(f"Hey {message.author} please don't use such language")
    

intents=discord.Intents.all() 
intents.message_content= True
intents.members=True
client=client(command_prefix="!",intents=intents)

GUILD_ID = discord.Object(id=1391791251031851110) # for insuring that the bot run in the specific server only

# Command that says hi to the user who ran it
@client.tree.command(name="hello",description="Say hi", guild=discord.Object(id=1391791251031851110))
async def say_hi(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hi {interaction.user.mention}")

# Command that prints user input
@client.tree.command(name="say",description="Print the user input",guild=discord.Object(id=1391791251031851110))
async def say_com(interaction:discord.Interaction,expression:str):
    await interaction.response.send_message(expression)

# ccommand practice
@client.tree.command(name="pingyourself", description="fun command",guild=discord.Object(id=1391791251031851110))
async def mention(interaction:discord.Interaction):
    await interaction.response.send_message(f"Son of mitch {interaction.user.mention}")

# kick command
@client.tree.command(name="kick",description="kick User",guild=discord.Object(id=1391791251031851110))
@app_commands.describe(user="The user to kick", reason="The reason for kicking")
async def kick(interaction:discord.Interaction,user:discord.Member,reason:str):
    # Permission check
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ You don't have permission to kick members.", ephemeral=True)
        return
    else:
            dm=client.get_user(user)
            await user.send(f"You have been kicked from the server")
            await user.kick(reason=reason)
            await interaction.response.send_message(f"{user} is been kicked due to the Reason:{reason}")

#Embed
# @client.tree.command(name="embed",description="create embeds",guild=discord.Object(id=1391791251031851110))
# async def embeds(interaction:discord.Interaction,title:str,description:str,url:str,image:str,thumbnail:str,footer:str,channel:str):
#     embed=discord.Embed(title=title,url=url,description=description, color=discord.Color.red())
#     embed.set_thumbnail(url=thumbnail)
#     embed.set_image(url=image)
#     # embed.add_field(name="Field 1",value="This is field 1",inline=False)
#     # embed.add_field(name="Field 2",value="This is field 2",inline=False)
#     embed.set_footer(text=footer)
#     embed.set_author(name=interaction.user.name,url="https://youtu.be/KHQ2MaDbx5I?si=aYUhuc5Hw-VDq6KW",icon_url="https://media.discordapp.net/attachments/1401105787127992350/1401106535915982949/Screenshot_2023-12-24_125547.png?")
#     await interaction.response.send_message(embed=embed)

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

# Embed sent to specific channel
@client.tree.command(name="embed2",description="create embeds",guild=discord.Object(id=1391791251031851110))
async def embed2(interaction:discord.Interaction,title:str,description:str,channel:discord.TextChannel):
    embed=discord.Embed(title=title,description=description,color=discord.Color.red())
    embed.set_footer(text="This is a footer")
    await channel.send(embed=embed)  # Send directly to selected channel
    await interaction.response.send_message(f"Embed sent to {channel.mention} ✅", ephemeral=True)

# Kick user with an embed
@client.tree.command(name="kicked",description="kick User",guild=discord.Object(id=1391791251031851110))
@app_commands.describe(user="The user to kick", reason="The reason for kicking")
async def kickembed(interaction:discord.Interaction,user:discord.Member,reason:str):
    embed2=discord.Embed(title="Kick User",description=f"{user} is been kicked from the server due to the reason: {reason}",color=discord.Color.red())
    embed2.set_image(url="https://tenor.com/view/spongebob-squarepants-get-out-kick-out-booted-bye-felicia-gif-13565963.gif")
    # Permission check
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ You don't have permission to kick members.", ephemeral=True)
        return
    else:
            dm=client.get_user(user)
            await user.send(f"You have been kicked from the server due to the reason: {reason}")
            await user.kick(reason=reason)
            await interaction.response.send_message(embed=embed2)



client.run(TOKEN)