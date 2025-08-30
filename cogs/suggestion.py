import discord
from discord.ext import commands
from discord import app_commands

class suggestionCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # Suggestion system
    @commands.Cog.listener() # Event listener in cogs
    async def on_message(self,message:discord.Message):
        if message.author==self.client.user:
            return
        else:
            if message.channel.id==1407063214096777276:
                store_message=message.content
                sembed=discord.Embed(title=f"{message.author.global_name} - {message.author._user.id}",description=store_message)
                await message.delete()
                ed_message=await message.channel.send(embed=sembed)
                await message.channel.create_thread(name=F"Suggestion Thread")
                
async def setup(client: commands.Bot):
    await client.add_cog(suggestionCog(client))