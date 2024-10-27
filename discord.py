import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ボットが死んでしまった！")

bot.run("TOKEN") ##他人にTOKENを共有すると、荒らしに使われる可能性があります
