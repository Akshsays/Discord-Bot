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
    

    @app_commands.command(name="find", description="Calculate bits and bytes")
    async def byt(self, interaction: discord.Interaction, bits: float, bytes: float):
        b1 = bits / 8
        b2 = bytes * 8
        await interaction.response.send_message(
            f"The given number of bits {bits} are equal to {b1} number of bytes",
            ephemeral=True
        )
        await interaction.followup.send(
            f"The given number of bytes {bytes} are equal to {b2} number of bits",
            ephemeral=True
        )

    # Bot Ping
    @app_commands.command(name="ping", description="Tells the ping of the bot")
    async def pong(self, interaction: discord.Interaction):
        latency = round(self.client.latency * 1000)  # ms
        await interaction.response.send_message(f"🏓 Bot ping: {latency}ms", ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(funCog(client))

