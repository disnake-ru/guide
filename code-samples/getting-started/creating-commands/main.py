import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(test_guilds=[1234, 5678])


@bot.event
async def on_ready():
    print("Бот готов!")


@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Понг!")


@bot.slash_command()
async def server(inter):
    await inter.response.send_message(
        f"Название сервера: {inter.guild.name}\nВсего участников: {inter.guild.member_count}"
    )


@bot.slash_command()
async def user(inter):
    await inter.response.send_message(f"Ваш тег: {inter.author}\nВаш ID: {inter.author.id}")


YOUR_BOT_TOKEN = os.environ["YOUR_BOT_TOKEN"]
bot.run("YOUR_BOT_TOKEN")
