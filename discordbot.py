import os
import requests
import discord
import responses
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#scopes = "user-library-read"
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
#                                               client_secret=clientSilent,
#                                              scope=scopes))

#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#results = spotify.artist_albums(birdy_uri, album_type='album')
#albums = results['items']
#while results['next']:
#    results = spotify.next(results)
#    albums.extend(results['items'])

#for album in albums:
#    print(album['name'])

dotaUpdateUrl = "https://isthepatchout.com"

print(dotaUpdateUrl)

def ReadTokens():
#    idFile = open("id.txt", "r")
#    cli_id = idFile.readline()
#    cli_tok = idFile.readline()
#    idFile.close()
#    print(cli_id)
#    cli_id = cli_id.split("=")[1]
#    print(cli_id)
#    cli_tok = cli_tok.split("=")[1]
#    return cli_id, cli_tok
#    #reads tokens from file, file looks like this
#    #client_secret=xxxxxx
#    #client_id=xxxxxx
    TOKEN = os.getenv('DISCORD_TOKEN')
    ID = os.getenv('DISCORD_ID')
    return TOKEN, ID


def SpotSearch():
    pass
def SpotDisplay():
    pass

#async def send_message(message, user_message):
#    try:
#        response = responses.get_response(user_message)
#        await message.author.send(response)
#    except Exception as e:
#        print(e)



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

        print(f'bro really said "{user_message}" ({channel})')
        await send_message(message, user_message)

        

    client.run(clientToken)



if __name__ == '__main__':
    runDiscordBot()
