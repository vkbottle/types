# vkbottle-types

Библиотека [VK API](https://dev.vk.com/ru/method) типов и методов для фреймворка [**vkbottle**](https://github.com/vkbottle/vkbottle)

Самую новую версию можно поставить с мастера:

```console
pip install -U https://github.com/vkbottle/vkbottle-types/archive/master.zip
```

Если вы обнаружили баг в типах - не создавайте issue здесь, создайте его в разделе [основного репозитория](https://github.com/vkbottle/vkbottle), добавив тег `vkbottle-types`.

Если вы в состоянии исправить эту проблему сами, то сделайте пулл реквест сами, пожалуйста. Можете упомянуть issue в [основном репозитории](https://github.com/vkbottle/vkbottle)


## Оригинальная схема

https://github.com/VKCOM/vk-api-schema

## Добавление патча для схемы (WIP)

Из-за того что разработчики вк недобросовестно подходят к публикации схемы и релизам в целом, был сделан патчер схемы.

Для того, чтобы создать новый патч, используется следующая команда:

```console
python3 -m patcher -m "Add users.get missing param_name"
```

## Генерация типов

Генератор написан `>=Python 3.10`, но типы, которые он генерирует, не используют новые тайп-хинты `>=Python 3.9` и поддерживаются на более старых версиях питона `<= Python 3.8`

```console
python3 -m generator
```

Подробнее как самому сгенерировать типы в [HOWTO](/HOWTO)