# vkbottle-types

Библиотека [VK API](https://dev.vk.ru/ru/method) типов и методов для фреймворка [**vkbottle**](https://github.com/vkbottle/vkbottle)

Установить с pypi:

[![pypi](https://img.shields.io/pypi/v/vkbottle-types.svg)](https://pypi.org/project/vkbottle-types/)

```console
pip install vkbottle-types
```

Самую новую версию можно поставить с мастера:

```console
pip install -U https://github.com/vkbottle/vkbottle-types/archive/master.zip
```

Если вы обнаружили баг в типах - не создавайте issue здесь, создайте его в разделе [основного репозитория](https://github.com/vkbottle/vkbottle), добавив тег `vkbottle-types`.

Если вы в состоянии исправить эту проблему сами, то сделайте pull request сами, пожалуйста. Можете упомянуть issue в [основном репозитории](https://github.com/vkbottle/vkbottle).


## Оригинальная схема


[![vk-api](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FVKCOM%2Fvk-api-schema%2Frefs%2Fheads%2Fmaster%2Fpackage.json&query=%24.version&label=vk%20api%20schema
)](https://github.com/VKCOM/vk-api-schema)

## Добавление патча для схемы (WIP)

Из-за того что разработчики вк недобросовестно подходят к публикации схемы и релизам в целом, был сделан патчер схемы.

Для того, чтобы создать новый патч, используется следующая команда:

```console
python3 -m patcher -m "Add users.get missing param_name"
```

## Генерация типов

Генератор написан `>=Python 3.10`, но типы, которые он генерирует, не используют новые тайп-хинты для поддержки `Python 3.9`.

```console
python -m generator
```

Подробнее как самому сгенерировать типы в [HOWTO](/HOWTO)
