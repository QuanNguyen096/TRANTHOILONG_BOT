import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('Địt mẹ mày Long'):
    await message.channel.send('Má mày')
  if message.content.startswith('You a stupid huh'):
    await message.channel.send('Fuck you!!!')


client.run(os.environ['TOKEN'])

