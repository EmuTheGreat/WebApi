# Парсер строительных смесей с сайта maxidom

## Описание проекта

Этот проект представляет собой веб-приложение на базе FastAPI, которое реализует CRUD-операции для работы с продуктами и использует WebSocket для реального времени уведомлений о действиях с продуктами. Приложение также поддерживает асинхронный парсинг данных с сайта с использованием `aiohttp` и `BeautifulSoup`.

### Основные функции:
- **CRUD-операции**: создание, чтение и удаление продуктов из базы данных.
- **WebSocket**: уведомления для клиентов о добавлении и удалении продуктов в реальном времени.
- **Парсинг продуктов**: асинхронный парсер для получения списка продуктов с сайта и сохранения их в базу данных.
- **База данных**: SQLite с использованием SQLAlchemy для асинхронных операций.

## Структура проекта

### **Backend**
- **FastAPI** — основа для реализации API.
- **SQLAlchemy** (с поддержкой асинхронных операций через `asyncpg` и `aiomysql`) — используется для работы с базой данных.
- **WebSocket** — для получения уведомлений в реальном времени.
- **`aiohttp` и `BeautifulSoup`** — для асинхронного парсинга данных с внешнего сайта.

## Установка

### 1. Клонировать репозиторий
```bash
git clone https://github.com/EmuTheGreat/WebApi.git
cd fastapi-websocket-crud
