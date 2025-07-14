import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Load cogs
async def load():
    await bot.load_extension("cogs.commands")

bot.loop.create_task(load())
bot.run(os.getenv("DISCORD_TOKEN"))

