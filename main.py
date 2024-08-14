import discord
from discord import app_commands
from discord.ext import commands
import asyncio
from core.bot import Bot


input = str(input("Token: "))





async def main():
    discord.utils.setup_logging()
    async with Bot() as bot:
        await bot.start(input, reconnect=True)


if __name__ == "__main__":
    asyncio.run(main())