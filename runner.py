#import ytdlp
#from ytdlp import Music
#from cogs.ytdlp import Music
import asyncio
import dotenv
import os
import discord
from discord.ext import commands

#class Prepass:
    #__slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume')


TOKEN = os.getenv('DISCORD_TOKEN')
async def runDiscordBot():
    #Pre = Prepass()
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    await load(bot)
    await bot.start(TOKEN)
    #await bot.load_extension('ytdlp')
    #@bot.event
    #async def on_ready():
    #    await bot.load_extension('cogs.ytdlp')
    #    print(f'{bot.name} is ready')
    #await bot.add_cog(Music()
    #Pre.bot = bot
    #MusicBot = ytdlp.Music(bot)
    
    #bot.run(TOKEN)
    print('test')
     
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandError):
            print(f'error occured!: {error}')

async def load(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    asyncio.run(runDiscordBot())
