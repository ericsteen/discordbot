import discord
from discord.ext import commands
import yt_dlp
import os
import dotenv
import subprocess

yt_opts = {
    'format': 'bestaudio', 
    'extract-audio': True,
    'output': ''
        }


TOKEN = os.getenv('DISCORD_TOKEN')
def runDiscordBot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)


    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has arrived')

    @bot.command()
    async def play(ctx, url):
        if ctx.author.voice:
            voice_channel = ctx.author.voice.channel
            voice_client = await voice_channel.connect()
            print('joined voice channel')
        else:
            print('failed to join voice channel')


        ytdl = yt_dlp.YoutubeDL(yt_opts)
        info = ytdl.extract_info(url, download=False)
        print(info)
        audio_url = info['formats'][0]['url']

        print(url)
        print(audio_url)
              #yt_dlp_info    = subprocess.Popen([
        yt_dlp_process = subprocess.Popen(['yt-dlp','-f','ba','-o','-', audio_url], stdout=subprocess.PIPE)
        bot_audio = discord.FFmpegPCMAudio(yt_dlp_process.stdout)
        voice_client.play(bot_audio)

        #ytdl = yt_dlp.YoutubeDL(yt_opts)
        #info = ytdl.extract_info(url, download=False)
        #audio_url = info['formats'][0]['url']
        #breakpoint()
        #voice_client.play(discord.FFmpegPCMAudio(audio_url))
        #stream = ytdl.download(url)
        #voice_client.play(discord.FFmpegOpusAudio(stream, *, executable='ffmpeg', pipe=True))

    @bot.command()
    async def stop(ctx):
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client:
            await voice_client.disconnect()

    bot.run(TOKEN)

if __name__ == '__main__':
    runDiscordBot()
