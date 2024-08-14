from __future__ import annotations


from typing import List


import discord
from discord.ext import *
from core.bot import Bot
from discord import *


_all__ = (
    "Terminall_Commands",
)


class Terminall_Commands:
    def __init__(self, bot: Bot):
        self.bot = bot
    
    async def first_commands(self, interaction: Interaction):
        command_list = ["info"]  
        embed = discord.Embed(title="Лист команд 1 разряда", colour=Colour.green())
        

        for i, command in enumerate(command_list, start=1):  
            embed.add_field(name=f"Команда {i}", value=command, inline=False)  

        await interaction.response.edit_message(embed=embed, content=None, view=None, attachments=None)