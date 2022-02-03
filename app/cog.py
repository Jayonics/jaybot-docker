# cog.py
import discord
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from discord_token import token
intents = discord.Intents.all()


class Slash(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot

	@cog_ext.cog_slash(name="test")
	async def _test(self, ctx: SlashContext):
		embed = Embed(title="Embed Test")
		await ctx.send(embed=embed)


def setup(bot: Bot):
	bot.add_cog(Slash(bot))
