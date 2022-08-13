import asyncio

import disnake
from disnake import TextInputStyle
from disnake.ext import commands

bot = commands.Bot()


@bot.slash_command()
async def tags_low(inter: disnake.AppCmdInter):
    """Отправляет модальное окно для создания тега, но с низкоуровневой реализацией."""
    await inter.response.send_modal(
        title="Create Tag",
        custom_id="create_tag_low",
        components=[
            disnake.ui.TextInput(
                label="Name",
                placeholder="Bar Tag",
                custom_id="название",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Description",
                placeholder="Lorem ipsum dolor sit amet.",
                custom_id="описание",
                style=TextInputStyle.paragraph,
            ),
        ],
    )
    try:
        modal_inter: disnake.ModalInteraction = await bot.wait_for(
            "modal_submit",
            check=lambda i: i.custom_id == "create_tag_low" and i.author.id == inter.author.id,
            timeout=300,
        )
    except asyncio.TimeoutError:
        # пользователь не отправил модальное , поэтому возникает ошибка таймаута
        # нам не нужно выполнять никаких действий, так что просто завершаем выполнение функции
        return

    embed = disnake.Embed(title="Создание  тега")
    for key, value in modal_inter.text_values.items():
        embed.add_field(name=key.capitalize(), value=value[:1024], inline=False)
    await modal_inter.response.send_message(embed=embed)


bot.run("YOUR_BOT_TOKEN")
