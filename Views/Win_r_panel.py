import discord
import json
from discord.ext import commands
from discord.ui import Modal
from Views.Enter import Enter
from core.bot import Bot






class Win_Panel(Modal):
    def __init__(self, bot: Bot):
        self.bot = bot
        super().__init__(title="Win R Panel", custom_id="pa")
        self.terminal_input = discord.ui.TextInput(
            label="Enter command name",
            placeholder="command name here",
            custom_id="terminal_input",
            required=True
        )
        self.add_item(self.terminal_input)
    
    async def on_submit(self, interaction: discord.Interaction):
        entered_value = self.terminal_input.value

        
        terminal_value = ["terminal", "Terminal", "Terminal ", "terminal ", "терминал", "Терминал", "Терминал ", "термиал "]
        if entered_value in terminal_value:
            embed = discord.Embed(title="Терминал", description="Для продолжения нажмите на кнопку Enter")
            await interaction.response.send_message(embed=embed, ephemeral=True, view=Enter(self.bot))
        else:
            await interaction.response.send_message(f"Команда **{entered_value}** не найдена Список команд ", ephemeral=True)