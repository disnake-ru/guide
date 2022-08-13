import disnake
from disnake.ext import commands

import datetime

bot = commands.Bot(command_prefix="!", test_guilds=[123456789])


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command()
async def fullembed(ctx):

    embed = disnake.Embed(
        title="Заголовок эмбеда",
        description="Описание эмбеда",
        color=disnake.Colour.yellow(),
        url="https://disnake.dev/",
        timestamp=datetime.datetime.now(),
    )

    embed.set_author(
        name="Автор эмбеда",
        url="https://disnake.dev/",
        icon_url="https://disnake.dev/assets/disnake-logo.png",
    )

    embed.set_thumbnail(url="https://disnake.dev/assets/disnake-logo.png")

    embed.set_image(url="https://disnake.dev/assets/disnake-thin-banner.png")

    embed.add_field(name="Обычный заголовок", value="Обычное значение", inline=False)

    embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
    embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
    embed.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)

    embed.set_footer(
        text="Футер эмбеда",
        icon_url="https://disnake.dev/assets/disnake-logo.png",
    )

    await ctx.send(embed=embed)


bot.run("YOUR_BOT_TOKEN")
