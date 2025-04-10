# Ask Hub - A Quora-like Q&A Platform Built with Django

Ask Hub is a simple yet powerful community-driven Q&A platform where users can register, ask questions, post answers, and like answers from others — inspired by Quora. Built using Django with a clean server-rendered flow and Bootstrap 5 for elegant styling.

---

## Features

- User authentication (register, login, logout)
- Ask questions with title and description
- Post answers to any question
- Like/unlike answers (one like per user per answer)
- View all recent questions on the home page
- Detailed question page with answers + answer form
- User dashboard showing their questions and answers
- Pagination for answers
- Clean and elegant UI with Bootstrap

---

## Tech Stack

- **Backend:** Django 5
- **Frontend:** Django templates + Bootstrap 5
- **Database:** SQLite (default), but easily configurable for Postgres/MySQL
- **Auth:** Django built-in auth system

---

## Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Sunil1208/ask-hub.git
cd ask-hub
```

### 2. Create Virtaul Environement and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Environment Variables
```bash
cp .env.template .env
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```
Visit [Local Server on port 8000](http://localhost:8000) to see the server in action.

## Sample User Actions

Register or log in
- Ask your first question
- View any question and post an answer
- Like an answer
- Visit your dashboard via the navbar