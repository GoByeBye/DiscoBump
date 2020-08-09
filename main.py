import discord, os, time
from discord.ext import commands
import asyncio

# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
# token = os.getenv("TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
token = "your_token"

bot = commands.Bot(command_prefix="$")


async def d1(ctx):
    while True:
        await ctx.send("!d bump")
        await asyncio.sleep(7230)


async def d2(ctx):
    while True:
        for i in ["dgp!bump", "dgp!bump", "dgp!bump", "ob!bump"]:
            await ctx.send(i)
            await asyncio.sleep(930)


async def d3(ctx):
    while True:
        await ctx.send("d!bump")
        await asyncio.sleep(10830)


@bot.event
async def on_ready():
    print("Auto Bumper Is Online!")


@bot.event
async def on_message(message):
    if message.author.id != your_id:
        return
    await bot.process_commands(message)


@bot.command()
async def d(ctx):
    asyncio.create_task(d1(ctx))
    asyncio.create_task(d2(ctx))
    asyncio.create_task(d3(ctx))


bot.run(token, bot=False)
