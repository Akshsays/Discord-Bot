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


GUILD_ID = discord.Object(id=1391791251031851110) # for insuring that the bot run in the specific server only


intents=discord.Intents.all()
intents.message_content = True
intents.members = True

    
client=myclient()
client.run(TOKEN)
