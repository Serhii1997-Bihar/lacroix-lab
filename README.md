# 🛍️ E-Commerce Clothing Store Platform

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

A modern, scalable, and full-featured e-commerce platform for an online clothing store, built with the **Python / Django** stack. The project supports the entire purchasing lifecycle: from item search and catalog browsing to order processing, customer communication, and store administration.

---

## 🌟 Key Features

### 👤 User Management & Profiles
- **Authentication & Authorization:** User registration, login, password recovery, and role-based access control.
- **Internal Messaging / Live Chat:** Direct communication between users and support or other platform members.

### 🛒 Shopping & Order Management
- **Interactive Catalog:** Item search by title and convenient page pagination.
- **Shopping Cart:** Real-time adding, quantity updates, and item removal.
- **Checkout Process:** Streamlined order creation and persistence.

### 🛡️ Administration & Team
- **Admin Dashboard:** Built-in custom/extended Django admin interface to manage the catalog, categories, and orders.
- **Staff Section:** Displays information regarding store staff and team members.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django framework
- **Database:** PostgreSQL
- **Infrastructure & Containerization:** Docker, Docker Compose
- **Web Server & Reverse Proxy:** Nginx
- **Frontend:** HTML5, CSS3, JavaScript / Django Templates

---

## 📐 Project Architecture

```text
├── cart/                # Django app for shopping cart management
├── main_app/            # Main Django project settings module
├── media/               # Uploaded media files (product images)
├── nginx/               # Nginx server configuration files and setup
├── shop/                # Django app for product catalog, search, and orders
├── static/              # Project static files (CSS, JavaScript, images)
├── templates/           # Global HTML templates
├── users/               # Django app for authorization, user profiles, and chat
├── .env                 # Environment variables file
├── .gitignore           # Git ignore patterns
├── docker-compose.yaml  # Container orchestration setup
├── dockerfile           # Docker build instructions for the Django app
├── manage.py            # Primary Django management script
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies and libraries