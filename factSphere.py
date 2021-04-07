import os
import random
import discord
from dotenv import load_dotenv

load_dotenv('settings.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

corruption = 0

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
    
        if corruption > 1000:
            fact_file = 'glitch.txt'
            corruption = 0
        else:
            fact_file = 'facts.txt'
            corruption += random.randint(1,5)

        with open(fact_file, 'r') as facts:
            list_facts = facts.readlines()
            rng_fact = random.choice(list_facts)
            print(rng_fact)
        print(corruption)

    state_fact = 'Fact: ' + rng_fact

    if fact.content.startswith('&fact'):
        await fact.channel.send(state_fact)

client.run(TOKEN)