from __future__ import annotations



import discord

from discord import *

from discord.ext import commands

from core.bot import Bot

import datetime


__all__ = (
    "TerminalCommands",
)

emoji1 = "<:emoji_77:1215712871976009788>"
emoji1 = "<:crypto:1215729173029593129>"
pyth = "<:Python:1211078918275072010>"
amvit_avatar = "<:emoji_97:1220638451204882432>"
pol = "<:PrivacyPolicy:1220641278207852584>"
rait = "<:1198240902691430421:1220641562493587487>"
ownerss = "<:1210994549162246254:1220677929143504956>"
imagess = "<:1210991163914592316:1220677939386126346>"
budilnik = "<:1210991176790974524:1220677991210811402>"
zachita = "<:1210992717681795152:1220678011494469743>"
opisanie = "<:1210993505917472799:1220678077324070922>"
chelovek = "<:1210992686211792997:1220678075432439819>"
botyara = "<:1210994289853734962:1220678255523270766>"
textchanels = "<:1210992701546299483:1220678254159990815>"
voicechaels = "<:1209496632580644915:1220678215568326727>"
categoria = "<:1210992798828859412:1220678217065693284>"
bostua = "<:1210994289853734962:1220678255523270766>"
lvlboost = "<:1210992734945542264:1220678218412195871>"
shop_emojies = "<:YokeShopping:1221122542878724236>"
nononon = "<:not:1221123833298292827>"
rolllle = "<:8744specialroles:1221133035555000484>"
shtrafereror = "<:bad:1221162196424462477>"

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
    async def server(self, interaction: Interaction):
        guild = interaction.guild
        owner = guild.owner

        verification_level = guild.verification_level
        verification_levels = {
            "none": "Нет",
            "low": "Низкий",
            "medium": "Средний",
            "high": "Высокий",
            "highest": "Самый Высокий"
        }

        verification_level_str = verification_levels.get(verification_level.name.lower(), "Неизвестный уровень")

        created_time = guild.created_at
        formatted_created_time = discord.utils.format_dt(created_time, style="R")
        description = guild.description
        member_count = guild.member_count
        await guild.chunk()
        human_count = sum(not member.bot for member in guild.members)
        bot_count = sum(member.bot for member in guild.members)
        channels = guild.channels
        text_channels_count = sum(1 for channel in channels if isinstance(channel, discord.TextChannel))
        voice_channels_count = sum(1 for channel in channels if isinstance(channel, discord.VoiceChannel))
        category_channels_count = sum(1 for channel in channels if isinstance(channel, discord.CategoryChannel))
        boost_level = guild.premium_tier
        boost_count = guild.premium_subscription_count
        user = interaction.user

        server_icon_url = str(guild.icon.url) if guild.icon else None

        embed = discord.Embed(
            title=f"Информация о сервере **{guild.name}**",
            description=f"{ownerss}  овнер: ***{owner.mention}***,\n"
                        f"{imagess} Изображение: [аватар]({server_icon_url}),\n"
                        f"{budilnik} Создан: {formatted_created_time},\n"
                        f"{zachita} Уровень защиты: {verification_level_str},\n"
        )
        embed.set_footer(
            text=f"Запрос от {user.display_name}",
            icon_url=user.avatar.url
        )

        bot = self.bot
        embed.set_thumbnail(url=bot.user.avatar.url)
        embed.add_field(name=f"Участники ({member_count})", value=f"{chelovek} Участников: {human_count}\n {botyara} Ботов: {bot_count}")
        embed.add_field(name=f"Каналы ({len(channels)})", value=f"{textchanels} Текстовые каналы: {text_channels_count}\n {voicechaels} Голосовые каналы: {voice_channels_count}\n {categoria} Категории: {category_channels_count}")
        embed.add_field(name=f"бусты {boost_count}", value=f"{bostua} бустов: {boost_count}\n {lvlboost} уровень: {boost_level}")
        await interaction.response.send_message(embed=embed)