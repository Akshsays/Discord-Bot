import discord
from discord.ext import commands
from discord import app_commands


GUILD_ID = discord.Object(id=1391791251031851110) 

class client(commands.Bot):
    async def on_ready(self):
        print(F'logged on as{self.user}!')
        try:
            synced = await self.tree.sync(guild=discord.Object(id=1391791251031851110))
            print(f"Synced {len(synced)} commands to the server {GUILD_ID}.")

        except Exception as e:
            print(f"Error syncing commands: {e}")

# Command that says hi to the user who ran it
@client.tree.command(name="hello",description="Say hi", guild=discord.Object(id=1391791251031851110))
async def say_hi(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hi {interaction.user.mention}")

@client.tree.command(name="basic embed",description="basic embed with title,description,field and footer")
async def embed(interaction:discord.Interaction,title:str,description:str,channel:discord.TextChannel):
    embed=discord.Embed(title=title,description=description)
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message(f"{interaction.user.mention} Sorry you can use this command",ephemeral=True)
    else:
        await channel.send(embed=embed)
        await interaction.response.send_message(f"Embed sent to {channel.mention}",ephemeral=True)

#Embed
# @client.tree.command(name="embed",description="create embeds",guild=discord.Object(id=1391791251031851110))
# async def emebeds(interaction:discord.Interaction,title:str,dscription:str,url:str,image:str,thumbnail:str,footer:str,channel:str):
#     embed=discord.Embed(title=title,url=url,description=description, color=discord.Color.red())
#     embed.set_thumbnail(url=thumbnail)
#     embed.set_image(url=image)
#     # embed.add_field(name="Field 1",value="This is field 1",inline=False)
#     # embed.add_field(name="Field 2",value="This is field 2",inline=False)
#     embed.set_footer(text=footer)
#     embed.set_author(name=interaction.user.name,url="",icon_url="")
#     await interaction.response.send_message(embed=embed)

# command practice
@client.tree.command(name="pingyourself", description="fun command",guild=discord.Object(id=1391791251031851110))
async def mention(interaction:discord.Interaction):
    await interaction.response.send_message(f"Son of mitch {interaction.user.mention}")

# Command that prints user input
# @client.tree.command(name="say",description="Print the user input",guild=discord.Object(id=1391791251031851110))
# async def say_com(interaction:discord.Interaction,expression:str):
#     await interaction.response.send_message(expression)



# kick command
# @client.tree.command(name="kick",description="kick User",guild=discord.Object(id=1391791251031851110))
# @app_commands.describe(user="The user to kick", reason="The reason for kicking")
# async def kick(interaction:discord.Interaction,user:discord.Member,reason:str):
#     # Permission check
#     if not interaction.user.guild_permissions.kick_members:
#         await interaction.response.send_message("❌ You don't have permission to kick members.", ephemeral=True)
#         return
#     else:
#             dm=client.get_user(user)
#             await user.send(f"You have been kicked from the server")
#             await user.kick(reason=reason)
#             await interaction.response.send_message(f"{user} is been kicked due to the Reason:{reason}")

intents=discord.Intents.all() 
intents.message_content= True
intents.members=True
client=client(command_prefix="!",intents=intents)     