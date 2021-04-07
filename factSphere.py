import os
import random
import discord
import dotenv

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
    settings='settings.env'
    dotenv.load_dotenv(settings)
    corruption = int(dotenv.get_key(settings, 'CORRUPTION'))

    #don't let the bot reply to itself
    if fact.author == client.user:
        return
    
    if corruption > 1000:
        fact_file = 'glitch.txt'
        dotenv.set_key(settings, 'CORRUPTION', str(0))
    else:
        fact_file = 'facts.txt'
        corruption += random.randint(1,10)
        dotenv.set_key(settings, 'CORRUPTION', str(corruption))

    with open(fact_file, 'r') as facts:
        list_facts = facts.readlines()
        rng_fact = random.choice(list_facts)

    state_fact = 'Fact: ' + rng_fact

    if fact.content.startswith('&fact'):
        await fact.channel.send(state_fact)

client.run(TOKEN)