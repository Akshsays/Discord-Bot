import discord
from discord.ext import commands
from discord import app_commands

class funCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
     # Dm user    
    @app_commands.command(name="dm", description="Testing DM")
    async def dm(self, interaction: discord.Interaction):
        await interaction.user.send("Hello there!")
    
    #


async def setup(client: commands.Bot):
    await client.add_cog(funCog(client))

