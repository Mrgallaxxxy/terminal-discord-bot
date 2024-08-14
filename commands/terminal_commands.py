from __future__ import annotations



import discord

from discord import *

from discord.ext import commands

from core.bot import Bot

import datetime


__all__ = (
    "TerminalCommands",
)

class TerminalCommands:
    def __init__(self, bot: Bot):
        self.bot = bot
    
    async def info(self, interaction: Interaction):
        user = interaction.user
        user_id = user.id
        joined_at = user.joined_at
        join_date = discord.utils.format_dt(joined_at, 'R')
        mention = user.mention
        name = user.name
        avatar_url = user.avatar.url if user.avatar else None
        top_role = user.top_role
                
        embed = Embed(
            title=f"Информация о {mention} | {name}",
            description=f"・ **ID**: {user_id}\n・ **Имя**: {name}\n・ **Дата вступления**: {join_date}\n・ **Упоминание**: {mention}",
            colour=discord.Colour.yellow()
        )
                
        if avatar_url:
            embed.set_thumbnail(url=avatar_url)
                
        embed.add_field(name="Высшая роль", value=f"{top_role}", inline=True)
        embed.set_footer(text=f"Запрос от {name} | {datetime.datetime.utcnow()}", icon_url=avatar_url)
                
        await interaction.response.send_message(embed=embed)