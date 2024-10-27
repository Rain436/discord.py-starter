import discord
from discord import app_commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'死んだ')
    await bot.tree.sync()  

@discordpypy.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

client.run("token")
