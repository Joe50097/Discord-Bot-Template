import discord
from discord import app_commands
from discord.ext import commands

class UtilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /help command
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="help", description="Get a list of available commands!")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Available Commands",
            description="Here are the commands you can use:",
            color=discord.Color.blue()
        )
        embed.add_field(name="`/help`", value="Get a list of available commands!", inline=False)
        embed.add_field(name="`/ping`", value="Check how fast the bot is at the moment! (Less ms means faster responses)", inline=False)
        embed.add_field(name="`/hello`", value="Say hello!", inline=False)
        
        embed.set_footer(text="Use /help to see this message again.")
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        await interaction.response.send_message(embed=embed)

    # /ping command
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="ping", description="Check how fast the bot is at the moment! (Less ms means faster responses)")
    async def ping(self, interaction: discord.Interaction):
        # calculate the latency between the bot and discord server
        latency = round(self.bot.latency * 1000)

        # create an embed message to display the latency
        embed = discord.Embed(
            title="🏓 Pong!",
            description="Here's the current latency:",
            color=discord.Color.blue()
        )
        embed.add_field(name="Latency", value=f"{latency}ms", inline=False)
        embed.set_footer(text="Latency check complete.")
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        # send the embed as a response to the interaction
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UtilityCog(bot))