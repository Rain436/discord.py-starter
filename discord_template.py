import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@discordpypy.event
async def on_ready():
    print("ボットが死んでしまった！")

client.run("TOKEN") ##他人にTOKENを共有すると、荒らしに使われる可能性があります
