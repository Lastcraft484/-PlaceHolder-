import discord
from discord.ext import commands
import json
import aiohttp
import random
import urllib.parse, urllib.request, re
from mcstatus import MinecraftServer
import config

bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)
async def youtube(ctx, *search):
    searchTerm = ' '.join(search)
    query_string = urllib.parse.urlencode({'search_query': searchTerm})
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


if __name__ == '__main__':
    import config
    bot.run(config.token)