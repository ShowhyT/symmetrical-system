import os
import discord

from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Бот готов к работе")


bot.run(os.getenv(TOKEN))
