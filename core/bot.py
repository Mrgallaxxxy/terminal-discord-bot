from __future__ import annotations



import discord
from discord.ext import commands
import os


__all__ = (
    "Bot",
)


class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix="T.",
            intents=discord.Intents.all()
        )
    
    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")
        print("------")
    
    async def on_connect(self):
        sync = await self.tree.sync()
        print(f"Synced commands: {len(sync)}")
        self.remove_command("help")
        print("Removing command help")
    
    async def setup_hook(self) -> None:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded cog: {filename[:-3]}")
                except Exception as e:
                    print(f"Failed to load cog {filename[:-3]}: {e}")
        