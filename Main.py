import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command()
async def ping():
    print(Pong!)

if __name__ == '__main__':
    import config
    bot.run(config.token)