import discord
from discord.ext import commands
import json
import aiohttp
import random
import urllib.parse, urllib.request, re
import config

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def youtube(ctx, *search):
    searchTerm = ' '.join(search)
    query_string = urllib.parse.urlencode({'search_query': searchTerm})
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


    import config
    bot.run(config.token)