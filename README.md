# GitHub Activity CLI
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Консольное приложение для просмотра активности пользователей GitHub

## Возможности

- 📊 Отображение активности пользователя GitHub
- 🎨 Цветной вывод
- ⚙️ Настраиваемая конфигурация
- 🔒 Поддержка GitHub API токенов для увеличения лимитов запросов
- 📝 Фильтрация по типам событий (Push, Issues, Pull Requests, и др.)
- ⏰ Настройка отображения времени событий
- 📦 Простая установка и использование

## 🛠 Установка

```bash
git clone https://github.com/NZT-48-Z/github-activity.git

cd github-activity

# На Windows
.\install.bat
# На Linux / macOS
chmod +x install.sh
./install.sh
```

## 🖥️ Использование
```bash
github-activity username

# Пересоздание конфига
github-activity --setup
github-activity -s
github-activity username --setup
```
### Пример
```bash
github-activity torvalds

Fetching activity for torvalds...
- Pushed 20 commits to torvalds/linux [2025-08-01 21:33]
- Pushed 20 commits to torvalds/linux [2025-08-01 17:33]
- Pushed 20 commits to torvalds/linux [2025-08-01 04:50]
- Pushed 10 commits to torvalds/linux [2025-08-01 00:37]
- Pushed 20 commits to torvalds/linux [2025-07-31 23:40]
```

## ⚙️ Конфигурация

Приложение создает файл config.json в текущей директории со следующими настройками:


```json
{
    "token": "",
    "limit": 50,
    "sort_order": "desc",
    "show_time": true,
    "event_types": [
        "PushEvent",
        "IssuesEvent",
        "PullRequestEvent",
        "WatchEvent",
        "ForkEvent",
        "CreateEvent"
    ]
}
```



### Параметры конфигурации

- **token** - GitHub API токен (опционально, но рекомендуется для увеличения лимитов)
- **limit** - Количество событий для отображения (по умолчанию 50)
- **sort_order** - Порядок сортировки: "desc" (новые сначала) или "asc" (старые сначала)
- **show_time** - Показывать ли время событий (true/false)
- **event_types** - Список типов событий для отображения

### Получение GitHub API токена

1. Перейдите на [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/personal-access-tokens)
2. Нажмите "Generate new token"
3. Выберите необходимые разрешения (public_repo)
4. Скопируйте токен и вставьте в конфигурацию
