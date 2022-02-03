import random

import discord
import os
import time

from discord import *
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(prefix='$', intents=intents)

import Gif_Ascii_Animator


# bot = discord.Bot(prefix='', intents=intents)
# bot = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def get_names(client):
	names = list()
	for user in client.guild.users:
		if user.game == None:
			print(user.name + " is not playing anything")
		else:
			print(member.name, member.id, user.game)


# Create a randomly generated bank account class
class BankAccount:
	def __init__(self, name, balance):
		self.card_number_string = None
		self.name = name
		self.balance = self.random_balance_generator()
		self.card_number = self.random_card_number_generator()

	def random_balance_generator(self):
		self.whole_part = random.randint(0, 1000)
		self.decimal_part = random.randint(0, 99)
		self.balance = self.whole_part + self.decimal_part / 100
		return self.balance

	def print_balance(self):
		return str('£' + str(self.balance))

	def random_card_number_generator(self):
		self.card_number = random.randint(1000000000000000, 9999999999999999)
		return self.card_number

	def print_card_number(self):
		# Convert card number to string
		self.card_number_string = str(self.card_number)

		# Split the card number into a string of 4 digit chunks
		self.card_number_string = self.card_number_string[0:4] + ' ' + self.card_number_string[4:8] + ' ' + self.card_number_string[8:12] + ' ' + self.card_number_string[12:16]
		return str(self.card_number_string)



@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

	if message.content.startswith('$Say what'):
		await message.channel.send('You want some? I\'ll give it ya!')
	elif message.content.startswith('$Say'):
		await message.channel.send(message.content[5:])

	if message.content.startswith('ICT' or 'Computer Science'):
		await message.channel.send('Computing is the best field. Prove me wrong.')

	if message.content.startswith('$playing'):
		owner = message.author
		if owner.activity is not None:
			await message.channel.send('You are playing ' + owner.activity.name)
		else:
			await message.channel.send('You are not playing anything')

	if message.content.startswith('$whoelseisplaying'):
		if message.author.activity is not None:
			for member in message.guild.members:
				members_playing_same_game = []
				if member.activity.name == message.author.activity.name:
					await message.channel.send(member.mention + ' is also playing ' + member.author.activity.name)
		else:
			await message.channel.send(message.author.mention + 'You\'re not playing anything!')

	if message.content.startswith('$stealcreditcards'):
		await message.channel.send('Processing...')
		starting_message = await message.channel.send('💳')
		while len(starting_message.content) < 5:
			time.sleep(0.25)
			# Duplicate the message content until it is 50 characters long
			await starting_message.edit(content=starting_message.content + '💳')
		# Create a fake bank account instance for each guild member.
		for member in message.guild.members:
			if member.status != discord.Status.offline and member.bot == False:
				time.sleep(0.25)
				bank_account = BankAccount(member.name, 0)
				await message.channel.send('Account Owner: ' + str(bank_account.name) + '\n' + '```' + 'Account Number: ' + str(bank_account.print_card_number()) + '\n' + 'Account Balance: ' + str(bank_account.print_balance()) + '```')
		await message.channel.send('Accounts stolen!')
		# Remove a character from the message content at the same rate until there is one character left
		while len(starting_message.content) > 1:
			time.sleep(0.25)
			await starting_message.edit(content=starting_message.content[:-1])

	if message.content.startswith('$goingonatrip'):
		speed = 0.1
		goingonatrip_first_message = await message.channel.send('🚗')
		while message.content.startswith('$endtrip') == False:
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗')
			time.sleep(speed)
			# Reverse the trip
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🛣' + '🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')
			time.sleep(speed)
			await goingonatrip_first_message.edit(content='🚗' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣' + '🛣')


@client.event
async def on_member_update(before, after):
	general_channel = client.get_channel(739058984100907904)
	if before.activities != after.activities:
		before_name = any(activity.name for activity in before.activities)
		after_name = any(activity.name for activity in after.activities)
		if not before_name and after_name:
			await general_channel.send(after.name + " is playing " + after_name)
			print(after.name + " is playing " + after_name)
		# await after.add_roles(role)
		elif before_name and not after_name:
			# await after.remove_roles(role)
			await general_channel.send(after.name + " is not playing " + before_name)
			print(after.name + " is not playing " + before_name)


client.run(os.getenv('TOKEN'))
