from imaplib import Commands
import discord
from discord.ext import commands
from aiohttp import request

class api_calls(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def neko(self, ctx):
        URL = "https://neko-love.xyz/api/v1/neko"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def kitsune(self, ctx):
        URL = "https://neko-love.xyz/api/v1/kitsune"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def hug(self, ctx):
        URL = "https://neko-love.xyz/api/v1/hug"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def pat(self, ctx):
        URL = "https://neko-love.xyz/api/v1/pat"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def waifu(self, ctx):
        URL = "https://neko-love.xyz/api/v1/waifu"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def cry(self, ctx):
        URL = "https://neko-love.xyz/api/v1/cry"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def kiss(self, ctx):
        URL = "https://neko-love.xyz/api/v1/kiss"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def slap(self, ctx):
        URL = "https://neko-love.xyz/api/v1/slap"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def smug(self, ctx):
        URL = "https://neko-love.xyz/api/v1/smug"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def punch(self, ctx):
        URL = "https://neko-love.xyz/api/v1/punch"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")

    @commands.command()
    async def nekolewd(self, ctx):
        URL = "https://neko-love.xyz/api/v1/nekolewd"
        async with request("GET", URL, headers = {}) as response:
            if response.status==200:
                embed = discord.Embed(colour=ctx.author.colour)
                data = await response.json()
                embed.set_image(url=data["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
    

def setup(client):
    client.add_cog(api_calls(client))