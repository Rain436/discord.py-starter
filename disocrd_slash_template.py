import discord
from discord import app_commands

intents = discord.Intents.default()
discordpypy = commands.Bot(command_prefix='!', intents=intents)

@discordpypy.event
async def on_ready():
    print(f'死んだ')
    await bot.tree.sync()  

@discordpypy.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

discordpypy.run("token")
