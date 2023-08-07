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


    async def player_loop(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            async with timeout(3):
                source = await self.queue.get()


    @commands.command(name='join', aliases=['connect','j'], description='connects to voice')
    async def connect(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            channel = ctx.author.voice.channel
        
        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
        else:
            await channel.connect()
            await ctx.send(f'**joined `{channel}`**')

    @commands.command(name='play', aliases=['sing','p'], description="plays stream from yt")
    async def play(self, ctx, *, search: str):
        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect)



