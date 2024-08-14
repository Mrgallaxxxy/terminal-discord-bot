import discord
from discord import app_commands
from core.bot import Bot
from discord.ext import commands
from  Views.help_button import *



class Help(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @app_commands.command(name="help", description="help with bot")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(title="help", description="Выберите кнопки ниже чтобы получить помощь по вашему запросу(или связаться с разработчиком )")
        embed.set_thumbnail(url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed, view=HelpButton(self.bot))


async def setup(bot):
    await bot.add_cog(Help(bot))