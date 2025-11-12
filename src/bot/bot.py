import discord
from discord.ext import commands
from .settings import settings

INTENTS = discord.Intents.default()
INTENTS.message_content = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=INTENTS)

    async def setup_hook(self):
        await self.load_extension("bot.cogs.core")


def run():
    bot = Bot()
    bot.run(settings.discord_token)


"""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Load GPT key
load_dotenv()
gpt_api_key = os.getenv("API_KEY")
client = OpenAI(api_key=gpt_api_key)
"""
