# Вклад

Во-первых, спасибо, что нашли время внести свой вклад. :+1:

В этом руководстве используется [`Docusaurus 2`](https://docusaurus.io/) для создания самого руководства и [`pre-commit`](https://pre-commit.com/) для различных задач форматирования/очистки - запуска содержимого через prettier, форматирования блоков кода Python и образцов и т.д.

Чтобы начать вносить свой вклад в это руководство, выполните следующие действия:

1. `cd guide` поскольку это наш каталог docusaurus.
2. Установите зависимости: `npm install`.
    - Примечание: Используйте Node версии 16.14 или выше.
3. Сборка с импользованием `Docusaurus`.
    - Чтобы создать документацию один раз, используйте `npm run build` и откройте `build/index.html` в вашем браузере.
    - В качестве альтернативы, если вы хотите видеть свои изменения в содержимом в режиме реального времени, используйте `npm run start`, чтобы запустить сервер на localhost.
4. Запустите `pre-commit`.
    - Если вы хотите установить хуки предварительной фиксации для автоматического запуска перед каждой фиксацией, используйте `pre-commit install`.
    - В противном случае используйте `pre-commit run --all-files`, чтобы выполнить все проверки один раз.
