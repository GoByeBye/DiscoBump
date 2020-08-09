import discord, os, time
from discord.ext import commands


# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
# token = os.getenv("TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
token = "ur_token_homo"

bot = commands.Bot(command_prefix="$", self_bot=True)

# Define the timeouts for the bumping shit
d = "10800"


@bot.event
async def on_ready():
    print("Auto Bumper Is Online!")


@bot.command()
async def d(ctx):
    while True:
        await ctx.send("d!bump")
        time.sleep(d)


bot.run(token, bot=False)
