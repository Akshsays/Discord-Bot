import discord
from discord.ext import commands
from discord import app_commands

class embedCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(
        name="embed",
        description="Basic embed with title, description, field and footer"
    )
    async def embed(self, interaction: discord.Interaction, title: str, description: str, channel: discord.TextChannel):
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.red()
        )
        # embed.set_footer(text="This is a footer")

        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message(
                f"{interaction.user.mention} Sorry, you can’t use this command.",
                ephemeral=True
            )
            return

        await channel.send(embed=embed)  # Send directly to selected channel
        await interaction.response.send_message(
            f"✅ Embed sent to {channel.mention}",
            ephemeral=True
        )

async def setup(client: commands.Bot):
    await client.add_cog(embedCog(client))