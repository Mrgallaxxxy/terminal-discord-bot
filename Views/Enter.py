from discord import *
from discord.ext import commands
from discord.ui import *
import discord
from .Terminal import Terminal
from core.bot import Bot




class Enter(View):
    def __init__(self, bot: Bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    @button(
        label="Enter",
        style=ButtonStyle.green,
        custom_id="enter_button"
    )
    async def enter_button(self, inter: Interaction, button: Button):
        await inter.response.send_modal(Terminal(self.bot))