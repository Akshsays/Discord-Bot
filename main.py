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


class myclient(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!", 
            intents=discord.Intents.all(), 
            application_id="1397268658878943353"
        )

    async def setup_hook(self):
        # Auto-load all cogs from ./cogs folder
        for fn in os.listdir("./cogs"):
            if fn.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{fn[:-3]}")
                    print(f"✅ Loaded extension: {fn}")
                except Exception as e:
                    print(f"❌ Failed to load {fn}: {e}")    

        # Sync commands
        try:
            guild = discord.Object(id=GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            print(f"✅ Synced {len(synced)} commands to {GUILD_ID}")

        except Exception as e:
            print(f"Error syncing commands: {e}")

    async def on_ready(self):
        print(f"Logged on as {self.user}")


# Message Events            

   # React to a message     
    # async def on_message(self,message):
    #     # print(f"Message from: {message.author}:{message.content}") 
    #     if message.content == "Syst":
    #         await message.channel.send("He is noob!!")

    # Send message on message edit
    # async def on_message_edit(self,before,after):
    #     if before.content!=after.content:
    #         await after.channel.send(f"{before.author} Edited there message:\n **Original:** {before.content}\n **Edited** {after.content}\n")               

    # Message on deleting
    # async def on_message_delete(self,message):
    #     if message.author==self.user:
    #         return
    #     else:
    #         await message.channel.send(f'I saw that {message.author}!!')

# Reaction events

    # Message on reaction       
    # async def on_reaction_add(self,reaction,user):
    #     if str(reaction.emoji) == "👍": 
    #         await reaction.message.channel.send(f'You reacted with this emoji :{reaction.emoji}!!')

    # Send message on removing reaction
    # async def on_reaction_remove(self,reaction,user):
    #     await reaction.message.channel.send("Why did you removed the reaction 🥀")

# User join and leave events

    # Welcome user when joined the server with and embed
    # async def on_member_join(self,member):
    #     channel = self.get_channel(1398593475250749450)
    #     embed=discord.Embed(title=f"📸 Lights, camera, action!",description=f"Welcome to **Basement** \n\n Get ready to supercharge your Discord server with our feature-rich bot. Join lively discussions, get help with ABOT, and connect with a friendly bunch of enthusiasts. Were excited to have you here.")
    #     if channel:
    #         await channel.send(f'{member.mention} landed here')
    #         await channel.send(embed=embed)

    # # Send message on user leaves
    # async def on_member_remove(self,member):
    #     channel=self.get_channel(1398594677065650206)
    #     if channel:
    #         await channel.send(f'{member.name} Left us 🥀')

    # async def on_member_banned(self,member):
    #     channel=self.get_channel(1398574226297982987)
    #     if channel:
    #         await channel.send(f"Bohaha {member.name} got banned")

# Small automod            
    
    # bad language
    # async def on_message(self,message):
    #         badwords=["fuck","dick","mf","shit"]
    #         mesg_content=message.content.lower()
    #         if any(word in mesg_content for word in badwords):
    #             await message.delete()
    #             await message.channel.send(f"Hey {message.author} please don't use such language")
    

GUILD_ID = discord.Object(id=1391791251031851110) # for insuring that the bot run in the specific server only


intents=discord.Intents.all()
intents.message_content = True
intents.members = True

# # Button response and style
# class View(discord.ui.View): 
#     @discord.ui.button(label="Click me",style=discord.ButtonStyle.red,emoji="🙃")
#     async def button_callback(self,button,interaction):
#         await button.response.send_message("You clicked the button",ephemeral=True)

#     #second button   
#     @discord.ui.button(label="Second button",style=discord.ButtonStyle.grey,emoji="🥀")
#     async def secondb_callback(self,button,interaction): # should give different function name for each button
#         await button.response.send_message("This was the second button",ephemeral=True)

# #Buttons send on slash cmd
# @client.tree.command(name="button",description="add a button",guild=discord.Object(id=1391791251031851110))
# async def buttons(interaction:discord.Interaction):
#     await interaction.response.send_message(view=View())

# # bits to bytes converter cmd
# @client.tree.command(name="find",description="Calculate bits and bytes",guild=discord.Object(id=1391791251031851110))
# async def byt(interaction:discord.Interaction,bits:float,bytes:float):
#     b1=bits/8
#     b2=bytes*8
#     await interaction.response.send_message(f"The given number of bits {bits} are equal to {b1} number of bytes",ephemeral=True)
#     await interaction.followup.send(f"The given number of byes {bytes} are equal to {b2} number of bits",ephemeral=True)

# # Bot ping
# @client.tree.command(name="ping",description="Tells the ping of the bot",guild=discord.Object(id=1391791251031851110))
# async def pong(interaction:discord.Interaction):
#     latency=round(client.latency*8)
#     await interaction.response.send_message(f"Bot ping: {latency}",ephemeral=True)



# # Add user a role
# @client.tree.command(name="addrole",description="Add a role to user",guild=discord.Object(id=1391791251031851110))
# async def addrole(interaction:discord.Interaction,user:discord.User,role:discord.Role):
#     if not interaction.user.guild_permissions.manage_roles:
#         await interaction.response.send_message(f"You don't have requires permission to use this command",ephemeral=True)
#     else:
#         await user.add_roles(role)
#         await interaction.response.send_message(f"Role Has been added to {user}",ephemeral=True)

# # Remove user role
# @client.tree.command(name="remove_role",description="Remove a role to user",guild=discord.Object(id=1391791251031851110))
# async def addrole(interaction:discord.Interaction,user:discord.User,role:discord.Role):
#     if not interaction.user.guild_permissions.manage_roles:
#         await interaction.response.send_message(f"You don't have requires permission to use this command",ephemeral=True)
#     else:
#         await user.remove_roles(role)
#         await interaction.response.send_message(f"Role Has been removed from {user}",ephemeral=True)


@commands.Cog.listener()    
async def on_message(self,message:discord.Message):
    if message.channel.id==1406545394472718438:
        await message.channel.create_thread(name="Support Thread")

    
client=myclient()
client.run(TOKEN)
