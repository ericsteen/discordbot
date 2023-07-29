import discord
from discord.ext import commands
import yt_dlp
import os
import dotenv
import subprocess
import logging

yt_opts = {
    'format': 'bestaudio', 
    'extract-audio': True,
    'output': ''
        }

ffmpeg_options = {

        }


TOKEN = os.getenv('DISCORD_TOKEN')
def runDiscordBot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    ytdlp_logs()

    @bot.event
    async def on_ready():
       print(f'{bot.user.name} has arrived')
       #await bot.load_extension('cogs.Music')
       await load_cogs(bot)
       print(f'this is {bot.user.name}')

    @bot.command()
    async def play(ctx, url):
        if ctx.author.voice:
            voice_channel = ctx.author.voice.channel
            voice_client = await voice_channel.connect()
            print('joined voice channel')
        else:
            print('failed to join voice channel')

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            song_info = ydl.extract_info(url, download=False)
        print(song_info["url"])
        ctx.voice_client.play(discord.FFmpegPCMAudio(song_info['url']))
        #ctx.voice_client.play(discord.FFmpegPCMAudio(song_info['url'], **ffmpeg_options))

    @bot.command()
    async def stop(ctx):
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client:
            await voice_client.disconnect()

    bot.run(TOKEN)

async def load_cogs(bot):
    for filename in os.listdir('./cogs'):
        if filename[:-3] == '.py':
            await bot.load_extension(f'cogs{filename[:-3]}')

def ytdlp_logs():
    logger = logging.getLogger('yt_dlp')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m%-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    runDiscordBot()
