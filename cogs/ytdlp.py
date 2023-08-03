import discord
from discord.ext import commands
import asyncio
import yt_dlp



ytdlp_opts = {
    'format':'bestaudio'
        }

ytdlp = yt_dlp.YoutubeDL(ytdlp_opts)

class musicPlayer():

    __slots__ = ('bot','guild','channel','cog')

    def __init__(self,ctx):
        self.bot = ctx.bot
        self.guild = ctx.guild
        self.channel = ctx.channel
        self.cog = ctx.cog
