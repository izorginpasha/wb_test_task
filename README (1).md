# Wildberries Product Analytics

Проект предназначен для парсинга товаров с Wildberries, их сохранения в базу данных и отображения на фронтенде с фильтрацией и графиками.

## 📦 Состав проекта

- **Backend (FastAPI)**:
  - Получает данные с сайта Wildberries
  - Сохраняет в PostgreSQL
  - API для получения товаров с фильтрацией
- **Frontend (React + Vite + Tailwind)**:
  - Таблица товаров с фильтрами и сортировкой
  - Графики: гистограмма цен и линейный график скидки/рейтинга

---

## 🚀 Запуск проекта

### 🔧 Требования

- Docker и Docker Compose
- Node.js (если запускать фронт отдельно)

---

### 🐳 Запуск через Docker Compose

```bash
docker-compose up --build
```

Контейнеры:

- `wb_app` — FastAPI-приложение
- `postgres` — база данных
- `pgadmin` — для просмотра данных (опционально)

---

### 🧪 Пример запроса

**GET** `http://localhost:8010/api/products/`

Параметры запроса:

| Параметр       | Тип     | Описание                                |
|----------------|----------|------------------------------------------|
| `name`         | `string` | Название товара (например, "кроссовки") |
| `min_price`    | `float`  | Минимальная цена                        |
| `max_price`    | `float`  | Максимальная цена                        |
| `min_rating`   | `float`  | Минимальный рейтинг                     |
| `min_feedbacks`| `int`    | Минимум отзывов                         |

---

### 🌐 Фронтенд

```bash
cd frontend
npm install
npm run dev
```

Запустится по адресу: [http://localhost:5173](http://localhost:5173)

Функции:

- Слайдеры и поля для фильтрации
- Динамическая таблица товаров
- Графики с данными на основе фильтров

---

## 📁 Структура проекта

```
wb_test_task/
│
├── backend/
│   ├── main.py
│   ├── api.py
│   ├── models.py
│   ├── db/
│   │   └── db.py
│   ├── schemas.py
│   └── parser.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── Filters.jsx
│   │   ├── ProductTable.jsx
│   │   ├── Charts.jsx
│   │   └── api/products.js
│   ├── index.css
│   └── vite.config.js
│
├── docker-compose.yml
└── README.md
```

---

## 📌 Примечания

- Если данные не найдены в БД — выполняется запрос к Wildberries.
- Используется FastAPI с асинхронной сессией SQLAlchemy.
- Для UI — TailwindCSS, графики — Recharts.