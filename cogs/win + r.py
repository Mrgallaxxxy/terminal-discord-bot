import discord
from discord import app_commands
from core.bot import Bot
from discord.ext import commands
from Views.Win_r_panel import Win_Panel


class WinR(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    groop = app_commands.Group(name="win", description="win r windows panel")
    
    @groop.command(name="r", description="win r windows panel")
    async def _r(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Win_Panel(self.bot))



async def setup(bot):
    await bot.add_cog(WinR(bot))
    