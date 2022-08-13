import disnake
from disnake.ext import commands
from disnake import TextInputStyle


bot = commands.Bot(command_prefix="!")


# Наследуем модальное окно
class MyModal(disnake.ui.Modal):
    def __init__(self):
        # Детали модального окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Name",
                placeholder="Foo Tag",
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
        ]
        super().__init__(
            title="Create Tag",
            custom_id="create_tag",
            components=components,
        )

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Создание тега")
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await inter.response.send_message(embed=embed)


@bot.slash_command()
async def tags(inter: disnake.AppCmdInter):
    """Отправляет модальное окно для создания тега"""
    await inter.response.send_modal(modal=MyModal())


bot.run("YOUR_BOT_TOKEN")
