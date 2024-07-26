# Import
import random
import discord
from discord.ext import commands
from pyjosa.josa import Josa
import yaml

# Set constants
TOKEN = '' # Put your bot token here!

# Load words
with open('words.yml', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

    who = data['who']
    item = data['item']
    verb = data['verb']

# Define functions
def make_response():
    response_type = random.randint(0, 2)

    if response_type == 0:
        response = f'{Josa.get_full_string(random.choice(who), "는")} {random.choice(verb)}하는 {random.choice(item)}.'
    elif response_type == 1:
        response = f'{Josa.get_full_string(random.choice(who), "는")} {random.choice(verb)}했다.'
    else:
        response = f'{Josa.get_full_string(random.choice(who), "는")} {Josa.get_full_string(random.choice(item), "으로")} {random.choice(verb)}했다.'

    response_type = random.randint(0, 1)

    if response_type == 0:
        response += f' 그건 마치 {random.choice(verb)}하는 {random.choice(item)}.'
    else:
        response += f' {random.choice(verb)}하는 {random.choice(item)}처럼.'

    return response

# Init discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot command
@bot.command('chat')
async def chat(ctx, *args):
    await ctx.send(make_response())

# Run app
bot.run(TOKEN)