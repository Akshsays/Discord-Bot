import discord
from discord.ext import commands
from discord import app_commands

class threadCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # Thread system
    @app_commands.command(name="thread",description="Creates thread")
    async def cthread(self,interaction:discord.Interaction,channel:discord.TextChannel,title:str):
        await channel.create_thread(name=title,type=discord.ChannelType.public_thread)
        await interaction.response.send_message(f"Thread created in {channel} channel", ephemeral=True)
    
    # Lock thread
    @app_commands.command(name="lock",description="lock thread")
    async def lthread(self,interaction:discord.Interaction):
        await interaction.channel.edit(locked=True)
        await interaction.response.send_message(f"The Thread is been locked",ephemeral=True)
        
    # Unlock thread
    @app_commands.command(name="unlock",description="Unlock thread")
    async def unthread(self,interaction:discord.Interaction):
        await interaction.channel.edit(locked=False)
        await interaction.response.send_message(f"The Thread is now unlocked",ephemeral=True)
    
    # Add user in thread
    @app_commands.command(name="addmember",description="Add user in thread channel")
    async def athread(self,interaction:discord.Interaction,user:discord.Member):
        await interaction.channel.add_user(user)
        await interaction.response.send_message(f"{user} is now added in thread channel",ephemeral=True)
    
    # Remove user from thread
    @app_commands.command(name="removemember",description="Remove user from thread channel")
    async def rthread(self,interaction:discord.Interaction,user:discord.Member):
        await interaction.channel.remove_user(user)
        await interaction.response.send_message(f"{user} is now added in thread channel",ephemeral=True)


async def setup(client: commands.Bot):
    await client.add_cog(threadCog(client))
