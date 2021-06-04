import os
import random
from quotes import Quotes
from datetime import date
from terminal_colors import bcolors

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

cache = {}
quotes = Quotes()
bot = commands.Bot(command_prefix='!')


@bot.command(name='craid', help='Bring all intelligence of ML and choose the best covenant in m+ especially for you!')
async def raid(ctx):
    await ctx.send(choose_quote(ctx))

@bot.command(name='ckeys', help='Bring all intelligence of ML and choose the best covenant in m+ specialy for you!')
async def keys(ctx):
    await ctx.send(choose_quote(ctx))

@bot.command(name='rl', help='Refresh quotes')
async def keys(ctx):
    quotes.load_quotes()


def build_cache_key(ctx):
    today = date.today()
    return f'{today}{ctx.author.name}{ctx.command}'

def choose_quote(ctx):
    cacheKey = build_cache_key(ctx)
    response = ''

    print(f"{bcolors.WARNING}--------------------------{bcolors.ENDC}")
    print(f"{bcolors.WARNING}{bcolors.BOLD}{ctx.author.name} - {bcolors.OKCYAN}{ctx.command}{bcolors.ENDC}")
    
    if cacheKey in cache:
        print(f"Used cache value:\n{bcolors.OKGREEN}{cacheKey}:{bcolors.ENDC} {cache[cacheKey]}")
        return  cache[cacheKey]
    else:
        general_quotes = []
        personal_quotes = []

        if ctx.author.name in quotes.personalized_quotes:
            personal_quotes = quotes.personalized_quotes[ctx.author.name]

        if ctx.command.name == 'craid':
            general_quotes = quotes.raid_quotes
        else:
            general_quotes = quotes.keys_quotes

        total_quotes = general_quotes + personal_quotes
        response = random.choice(general_quotes + personal_quotes)
        cache[cacheKey] = response
        print(f"Added to cache: \n{bcolors.WARNING}{cacheKey}:{bcolors.ENDC} {response}")

        return response

bot.run(TOKEN)