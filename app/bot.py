import discord
import random
import os
from discord import Intents, Embed
from discord.ext import commands
from discord.ext.commands import Bot, Cog
from discord_token import token
from discord_slash import SlashCommand, SlashContext, cog_ext

intents = discord.Intents.all()

# Note that command_prefix is a required but essentially unused paramater.
# Setting help_command=False ensures that discord.py does not create a !help command.
# Enabling self_bot ensures that the bot does not try and parse messages that start with "!".
bot = Bot(command_prefix="$", intents=intents)
slash = SlashCommand(bot)

bot.load_extension("cog")
bot.run(token)
