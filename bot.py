import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# define the intents
intents = discord.Intents.default()
intents.message_content = True # enable message content intent
intents.presences = True # enable presence intent
intents.members = True # enable server members intent

# bot instance
bot = commands.AutoShardedBot(intents=intents, command_prefix=None, help_command=None)

# bot Token
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="/help ✨"))
    print(f'{bot.user.name} is online! ✨')
    shards = bot.shard_count or 1
    print(f"Running on {shards} shard(s)")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# /help command
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="help", description="Get a list of available commands!")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Available Commands",
        description="Here are the commands you can use:",
        color=discord.Color.blue()
    )
    embed.add_field(name="`/help`", value="Get a list of available commands!", inline=False)
    embed.add_field(name="`/ping`", value="Check how fast the bot is at the moment! (Less ms means faster responses)", inline=False)
    embed.add_field(name="`/hello`", value="Say hello!", inline=False)
    
    embed.set_footer(text="Use /help to see this message again.")
    embed.set_thumbnail(url=bot.user.avatar.url)

    await interaction.response.send_message(embed=embed)

# /ping command
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="ping", description="Check how fast the bot is at the moment! (Less ms means faster responses)")
async def ping(interaction: discord.Interaction):
    # calculate the latency between the bot and discord server
    latency = round(bot.latency * 1000)

    # create an embed message to display the latency
    embed = discord.Embed(
        title="🏓 Pong!",
        description="Here's the current latency:",
        color=discord.Color.blue()
    )
    embed.add_field(name="Latency", value=f"{latency}ms", inline=False)
    embed.set_footer(text="Latency check complete.")
    embed.set_thumbnail(url=bot.user.avatar.url)

    # send the embed as a response to the interaction
    await interaction.response.send_message(embed=embed)

# /hello command
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(
        title="A Friendly Wave 👋",
        description="I hope you're doing well today! 🌟",
        color=discord.Color.blue()
    )
    embed.set_footer(text="Stay awesome!")
    embed.set_thumbnail(url=bot.user.avatar.url)

    # Send a personalized text message with the mention, followed by the embed
    await interaction.response.send_message(f"hello {interaction.user.mention}!", embed=embed)

bot.run(TOKEN)
