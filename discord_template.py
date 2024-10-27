import discord
from discord.ext import commands

intents = discord.Intents.all()
discordpypy = commands.Bot(command_prefix="!", intents=intents)

@discordpypy.event
async def on_ready():
    print("ボットが死んでしまった！")

discordpypy.run("TOKEN") ##他人にTOKENを共有すると、荒らしに使われる可能性があります
