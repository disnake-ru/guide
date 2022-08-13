import disnake
from disnake.ext import commands

import datetime

bot = commands.Bot(command_prefix="!", test_guilds=[123456789])


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command()
async def dictembed(ctx):

    embed_dict = {
        "title": "Заголовок эмбеда",
        "description": "Описание эмбеда",
        "color": 0xFEE75C,
        "timestamp": datetime.datetime.now().isoformat(),
        "author": {
            "name": "Автор эмбеда",
            "url": "https://disnake.dev/",
            "icon_url": "https://disnake.dev/assets/disnake-logo.png",
        },
        "thumbnail": {"url": "https://disnake.dev/assets/disnake-logo.png"},
        "fields": [
            {"name": "Обычный заголовок", "value": "Обычное значение", "inline": "false"},
            {"name": "Встроенный заголовок", "value": "Встроенное значение", "inline": "true"},
            {"name": "Встроенный заголовок", "value": "Встроенное значение", "inline": "true"},
            {"name": "Встроенный заголовок", "value": "Встроенное значение", "inline": "true"},
        ],
        "image": {"url": "https://disnake.dev/assets/disnake-thin-banner.png"},
        "footer": {
            "text": "Футер эмбеда",
            "icon_url": "https://disnake.dev/assets/disnake-logo.png",
        },
    }

    await ctx.send(embed=disnake.Embed.from_dict(embed_dict))


bot.run("YOUR_BOT_TOKEN")
