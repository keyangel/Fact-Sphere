import os
import random
import discord
import dotenv

dotenv.load_dotenv('settings.env')
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
async def on_message(message):
    settings='settings.env'
    dotenv.load_dotenv(settings)
    corruption = int(dotenv.get_key(settings, 'CORRUPTION'))
    stat_pc = corruption / 10
    stat_rep = 'Memory fragmentation at ' + str(stat_pc) + '%'

    #don't let the bot reply to itself
    if message.author == client.user:
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

    if message.content.startswith('&fact'):
        await message.channel.send(state_fact)

    if status.content.startswith('&status'):
        await status.channel.send(stat_rep)

client.run(TOKEN)