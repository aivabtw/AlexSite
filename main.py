import discord
from discord.ext import commands, tasks
import mains
import os

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="/")
mains.keep_alive()
bot.run(os.environ.get('bots'))
