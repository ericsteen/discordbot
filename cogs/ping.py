import discord
from discord.ext import commands

class ytdlp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_read(self):
        print('ready')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")


async def setup(bot):
    await bot.add_cog(ytdlp(bot))

