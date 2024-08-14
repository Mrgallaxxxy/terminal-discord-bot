from __future__ import annotations


from discord.ui import *
from discord.ext import *
from discord import *
import discord
from core.bot import Bot
from commands.list_command import *

__all__ = (
    "HelpButton",
    "LvlButtons"
)

class LvlButtons(View):
    def __init__(self, bot: Bot):
        self.bot = bot
        super().__init__(timeout=None)
    
    @button(
        label="1 Разряд",
        custom_id="low"
    )
    async def low(self, inter: Interaction, button: Button):
        term_command = Terminall_Commands(self.bot)
        await term_command.first_commands(interaction=inter)


class HelpButton(View):
    def __init__(self, bot: Bot):
        self.bot = bot
        super().__init__(timeout=None)
    
    
    
    @button(
        label="Список команд",
        custom_id="list"
    )
    async def list(self, inter: Interaction, button: Button):
        await inter.response.edit_message(embed=Embed(title="Список команд", description=f"> снизу нажав на кнопку вы **можете** выбрать разряд команд для **просмотра**"), view=LvlButtons(self.bot))