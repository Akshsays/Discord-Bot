import discord
from discord.ext import commands
from discord import app_commands

class roleCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # Add user a role
    @app_commands.command(name="addrole",description="Add a role to user")
    async def addrole(self,interaction:discord.Interaction,user:discord.User,role:discord.Role):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message(f"You don't have requires permission to use this command",ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"Role Has been added to {user}",ephemeral=True)
           
            # Remove user role
    @app_commands.command(name="remove_role",description="Remove a role to user")
    async def removerole(self,interaction:discord.Interaction,user:discord.User,role:discord.Role):
        if not interaction.user.guild_permissions.manage_roles:
                    await interaction.response.send_message(f"You don't have requires permission to use this command",ephemeral=True)
        else:
             await user.remove_roles(role)
             await interaction.response.send_message(f"Role Has been removed from {user}",ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(roleCog(client))
