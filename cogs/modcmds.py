import discord
from discord.ext import commands
from discord import app_commands
import datetime

class modCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
 # Kick user
    @app_commands.command(name="kick", description="kick User")
    @app_commands.describe(user="The user to kick", reason="The reason for kicking")
    async def kickembed(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        embed2 = discord.Embed(
            title="Kicked User",
            description="kicked the user from the server",
            color=discord.Color.red()
        )
        embed2.add_field(name=f"User:{user.name}", value=f"Reason:{reason}", inline=False)
        embed2.set_image(
            url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXNwdGZlcDNpcDNwNng1b2QxN3A2bjh4eG8wNmRhM241Mzl1c3N5cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UfkfLErH5QMlzXChcF/giphy.gif"
        )

        # Permission check
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("❌ You don't have permission to kick members.", ephemeral=True)
            return

        channel = interaction.guild.get_channel(1398574226297982987)
        dm = self.client.get_user(user.id)
        await user.send(f"You have been kicked from the server due to the reason: {reason}")
        await user.kick(reason=reason)
        if channel:
            await channel.send(embed=embed2)
        await interaction.response.send_message("User Successfully kicked", ephemeral=True)

    # Ban user
    @app_commands.command(name="ban", description="Ban user")
    async def ban(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You don't have required permission to use this command", ephemeral=True)
            return

        dm = self.client.get_user(user.id)
        await user.send(f"You have been banned from the server due to: {reason}")
        await user.ban(reason=reason)
        await interaction.response.send_message(f"{user} is banned from the server", ephemeral=True)

    # Unban user
    @app_commands.command(name="unban", description="Unban user")
    async def unban(self, interaction: discord.Interaction, user_id: int, reason: str):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You don't have required permission to use this command", ephemeral=True)
            return

        user = await self.client.fetch_user(user_id)
        await interaction.guild.unban(user, reason=reason)
        await interaction.response.send_message("Unbanned from the server", ephemeral=True)

    # Timeout user
    @app_commands.command(name="timeout", description="Timeout user")
    async def timeout(self, interaction: discord.Interaction, user: discord.Member, duration: int, reason: str):
        if not interaction.user.guild_permissions.mute_members:
            await interaction.response.send_message("You don't have required permission to use this command", ephemeral=True)
            return

        until_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=duration)
        await user.timeout(until_time, reason=reason)
        await interaction.response.send_message(f"{user.mention} Has been muted for {duration} minutes", ephemeral=True)

    # Remove timeout
    @app_commands.command(name="unmute", description="Remove user timeout")
    async def unmute(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        if not interaction.user.guild_permissions.mute_members:
            await interaction.response.send_message("You don't have required permission to use this command", ephemeral=True)
            return

        await user.timeout(None, reason=reason)
        await interaction.response.send_message(f"{user.mention} Has been unmuted", ephemeral=True)

    # Report command
    @app_commands.command(name="report", description="Report the user")
    @app_commands.describe(message="Enter the message to be reported", user="Enter user to report", reason="Enter the reason", comment="Add extra info")
    async def report(self, interaction: discord.Interaction, user: discord.Member, message: str, reason: str, comment: str):
        rpembed = discord.Embed(
            title="Report",
            description=f"{interaction.user.mention} reported {user} for {reason}",
            color=discord.Color.red()
        )
        rpembed.add_field(name="Message / Evidence", value=message, inline=False)
        rpembed.add_field(name="Comment", value=comment, inline=False)

        channelid = 1404893284890837013
        targetchannel = self.client.get_channel(channelid)
        if targetchannel:
            await targetchannel.send(embed=rpembed)
        await interaction.response.send_message(f"{interaction.user.mention} Thanks for reporting the user!!", ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(modCog(client))
