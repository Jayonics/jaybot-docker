import discord
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from discord_token import token

intents = discord.Intents.all()
bot = Client(intents=intents)
slash = SlashCommand(bot)


@slash.slash(name="test")
async def test(ctx: SlashContext):
	embed = Embed(title="Embed Test")
	await ctx.send(embed=embed)


bot.run(token)
