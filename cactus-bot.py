import discord
import os
import discord

from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Heya, pardner!')

print(TOKEN)
client.run(TOKEN)