import os
import random
import discord
from dotenv import load_dotenv

load_dotenv('settings.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to:\n'
            f'{guild.name} (id: {guild.id})'
        )

@client.event
async def on_message(fact):
    #don't let the bot reply to itself
    if fact.author == client.user:
        return
    
    with open('facts.txt', 'r') as facts:
    list_facts = facts.readlines()
    rng_fact = random.choice(list_facts)

    if fact.content.startswith('&fact'):
        await fact.channel.send('Fact:', rng_fact)

client.run(TOKEN)