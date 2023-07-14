1import os
import requests
import discord
import responses
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

dotaUpdateUrl = "https://isthepatchout.com"

print(dotaUpdateUrl)

ytdl_opts={
    'format': 'bestaudio/best',
    'outtmpl': 'tmp/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'default_search':'auto',
    'source_address': '0.0.0.0'
        }
ytdl = YoutubeDL(ytdl_opts)


def ReadTokens():
    TOKEN = os.getenv('DISCORD_TOKEN')
    ID = os.getenv('DISCORD_ID')
    return TOKEN, ID


def SpotSearch():
    pass
def SpotDisplay():
    pass

def runDiscordBot():
    clientToken, clientID = ReadTokens()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is online')

    async def send_message(message, user_message):
        try:
            response = responses.get_responses(user_message)
            await message.channel.send(response)
        except Exception as e:
            print(e)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        if user_message == "$devices" and message.author.voice:
            voice_client = discord.utils.get(client.voice_clients)
            audio_sources = voice_client.source.audio_source
            print("AUDIO_SOURCES: ")
            for audio_source in audio_sources:
                print(audio_source.title)
            
            audio_sources = voice_client.source.audio_source
        print(f'bro really said "{user_message}" ({channel})')
        await send_message(message, user_message)


    @client.event
    async def on_member_join(member):
        print(f'{member} joined')
        await message.channel.send('{member} has joined. Another wanderer, here to lick my father\'s boots. Good job')

        
    print(clientToken)
    client.run(clientToken)



if __name__ == '__main__':
    runDiscordBot()
