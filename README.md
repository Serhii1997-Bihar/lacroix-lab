# 🛍️ E-Commerce Clothing Store Platform

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

Сучасна, масштабована та повнофункціональна вебплатформа для інтернет-магазину одягу, побудована на стекi **Python / Django**. Проєкт підтримує повний цикл купівлі: від пошуку та каталогу товарів до оформлення замовлення, комунікації з клієнтами та адміністрування.

---

## 🌟 Ключові можливості (Key Features)

### 👤 Користувачі та Профіль
* **Автентифікація та Авторизація:** Реєстрація, вхід, відновлення пароля та розмежування прав доступу.
* **Внутрішній чат / Листування:** Можливість прямого спілкування користувачів з підтримкою або іншими учасниками платформи.

### 🛒 Шопінг та Замовлення
* **Інтерактивний каталог:** Пошук товарів за назвою та зручна пагінація сторінок.
* **Кошик покупок (Cart):** Додавання, редагування кількості та видалення товарів у реальному часі.
* **Оформлення замовлення (Checkout):** Зручний процес створення та збереження замовлень.

### 🛡️ Адміністрування та Команда
* **Панель управління:** Вбудована кастомна/розширена адмінка Django для управління каталогом, категоріями та замовленнями.
* **Секція працівників:** Відображення інформації про команду та персоналу магазину.

---

## 🛠️ Технологічний стек (Tech Stack)

* **Backend:** Python, Django framework
* **Database:** PostgreSQL
* **Infrastructure & Containerization:** Docker, Docker Compose
* **Web Server & Reverse Proxy:** Nginx
* **Frontend:** HTML5, CSS3, JavaScript / Django Templates

---

## 📐 Архітектура проєкту (Project Architecture)

```text
├── cart/                # Django-додаток для управління кошиком покупок
├── main_app/            # Основний модуль налаштувань проєкту Django
├── media/               # Завантажені медіафайли (зображення товарів)
├── nginx/               # Конфігураційні файли та налаштування Nginx
├── shop/                # Django-додаток каталогу товарів, пошуку та замовлень
├── static/              # Статичні файли проєкту (CSS, JavaScript, зображення)
├── templates/           # Загальні HTML-шаблони
├── users/               # Django-додаток для авторизації, профілів та чату
├── .env                 # Файл із змінними оточення
├── .gitignore           # Ігноровані файли для Git
├── docker-compose.yaml  # Конфігурація оркестрації контейнерів
├── dockerfile           # Інструкція збірки Docker-образу для Django
├── manage.py            # Головний скрипт управління Django
├── README.md            # Документація проєкту
└── requirements.txt     # Залежності та бібліотеки Python