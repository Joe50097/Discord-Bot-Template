import discord
import asyncio
import os
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

# load all the cogs
async def load_all_cogs():
    loaded_cogs = []
    failed_cogs = []
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                loaded_cogs.append(filename)
            except Exception as e:
                failed_cogs.append((filename, str(e)))
    if loaded_cogs:
        print("Loaded cog(s): " + ", ".join(loaded_cogs))
    if failed_cogs:
        for fname, err in failed_cogs:
            print(f"Failed to load cog {fname}: {err}")

async def main():
    await load_all_cogs()
    await bot.start(TOKEN)

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

if __name__ == "__main__":
    asyncio.run(main())
