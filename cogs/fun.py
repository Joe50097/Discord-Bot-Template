import discord
from discord import app_commands
from discord.ext import commands

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /hello command
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.command(name="hello", description="Say hello!")
    async def hello(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="A Friendly Wave 👋",
            description="I hope you're doing well today! 🌟",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Stay awesome!")
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        # Send a personalized text message with the mention, followed by the embed
        await interaction.response.send_message(f"hello {interaction.user.mention}!", embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(FunCog(bot))