import discord
from discord import Interaction, Embed
from discord.ui import Modal, TextInput
import json
import datetime
from core.bot import Bot
from commands.terminal_commands import TerminalCommands

class Terminal(Modal):
    def __init__(self, bot: Bot):
        self.bot = bot
        super().__init__(title="Terminal", custom_id="terminal")
        self.command = TextInput(label="Команда", placeholder="команда для терминала", custom_id="command", required=True)
        self.add_item(self.command)
    
    async def on_submit(self, interaction: Interaction):
        command_value = self.command.value  
        
        
        commands_of_terminal = TerminalCommands(self.bot)
        if command_value in ["info", "Info", "info ", "Info "]:
              await commands_of_terminal.info(interaction=interaction)
            
        else:
            await interaction.response.send_message(content=f"Команда **{command_value}** не найдена", ephemeral=True)
