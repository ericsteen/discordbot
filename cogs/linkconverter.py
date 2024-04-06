import discord
from discord.ext import commands

class linkconverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Link converter online')

    @commands.Cog.listener()
    async def on_message(self, message):
        #if message.author == Client.user:
        if message.author.bot:
            return
        link = message.content
        if 'https://tiktok.com' in link:
            new_link = link.replace('//tiktok.com', '//vxtiktok.com')
            await message.channel.send(new_link)
            await message.delete()
            print('replacing link')
            
        elif 'https://twitter.com' in link:
            new_link = link.replace('//twitter.com', '//vxtwitter.com')
            await message.channel.send(new_link)
            await message.delete()
            print('replacing link')
   #for ddinstagram, if you append /8 you get the 8th image in a collection 
        elif 'https://www.instagram.com' in link:
            new_link = link.replace('//www.instagram.com', '//d.ddinstagram.com')
            print(new_link)
            await message.channel.send(new_link)
            await message.delete()
            print('replacing link')


async def setup(bot):
    await bot.add_cog(linkconverter(bot))
