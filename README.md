# InstaScape 
**InstaScape** – скрипт для получения cookies из [Instagram](https://www.instagram.com/) в формате Netscape.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать.

2. Установить [Python](https://www.python.org/downloads/) версии 3.11 и выше. Рекомендуется добавить в PATH.

3. Открыть каталог со скриптом в консоли: можно воспользоваться командой cd или встроенными возможностями файлового менеджера.

4. Создать виртуальное окружение Python.

```
python -m venv .venv
```

5. Активировать вирутальное окружение.

#### Для Windows.
    
```shell
.venv\Scripts\activate.bat
```

#### Для Linux или MacOS.

```bash
source .venv/bin/activate
```

6. Установить зависимости скрипта.

```
pip install -r requirements.txt
```

7. Настроить бота путём редактирования _Settings.json_.

### Settings.json.

```JSON
"login": ""
```

Логин от аккаунта Instagram.

```JSON
"password": ""
```

Пароль от аккаунта.

```JSON
"path": ""
```
Место сохранения файла cookies, указывается обязательно. Если папки и/или файла не существует, создание пути, указанного пользователем происходит автоматически.

```JSON
"proxy": ""
```

Если требуется использование proxy, введите логин, пароль, IP-адрес и порт. Пример: **https://username:password@192.168.1.1:8080**.

8. Запустить файл _main.py_.

```
python main.py
```

---
**_Copyright © Dub Irina. 2024-2025._**
