# vkbottle-types

Библиотека типизации `vkbottle`. Самую новую версию можно поставить с мастера:

```shell script
pip install -U https://github.com/vkbottle/vkbottle-types/archive/master.zip
```

Если вы обнаружили баг в типах - не создавайте issue здесь, создайте его в разделе основного репозитория, добавив тег `vkbottle-types`

Если вы в состоянии исправить эту проблему сами, сделайте пулл реквест сами, пожалуйста. Можете упомянуть issue в основном репозитории


## Оригинальная схема

https://github.com/VKCOM/vk-api-schema

## Добавление патча для схемы

Из-за того что разработчики вк недобросовестно подходят к публикации схемы и релизам в целом, был сделан патчер схемы.

Для того чтобы создать новый патч:

```
python3 -m patcher -m "Add users.get missing param_name"
```

## Генерация типов

Генератор написан Python 3.10+, но типы которые он генерирует не используют новые тайп-хинты и поддерживаются на более старых версиях питона.

```
python3 -m generator
```

Подробнее как самому сгенерировать типы в [HOWTO](/HOWTO)

