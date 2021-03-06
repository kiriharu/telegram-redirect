## Легкий и настраиваемый сервис перенаправления Telegram, написанный на Flask.

### Возможности:
* Использует Bootstrap 4, полностью адаптивен.
* Легко настраивается, все сообщения можно настроить в config.py.
* Конфиг продукоментирован, разобраться сможет каждый.
* Возможность подключения Google Analytics.
* Имеет банлист ссылок/чатов/стикерпаков/ip адресов прокси (причину бана можно указывать тоже)
* Собственная и легкая система рекламы, вся база данных хранится в sqlite, написано с использованием Peewee. (её тоже можно отключать)
* ...и еще огромное количество возможностей!

### Установка:
Склонируйте репозиторий или скачайте и распакуйте архив:

```
https://github.com/kiriharu/telegram-redirect
```

Установите зависимости:

```
pip3 install -r requirments.txt
```

В config.py измените настройки под ваши нужды.
По стандарту - стоит изменить hostname на имя вашего сайта.

Запустите!

```
python3 app.py
```

### Скриншоты

![Main page](https://github.com/kiriharu/telegram-redirect/blob/master/tg1.png)
![Redirect page](https://github.com/kiriharu/telegram-redirect/blob/master/tg2.png)
