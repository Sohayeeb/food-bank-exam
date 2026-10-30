# AntiCode Rations — Community Food Bank

A Python-based Community Food Bank Management System built for the **Python Final Exam 2026**.

**Student:** ThinkShield  
**Project:** Community Food Bank Management System  
**Language:** Python 3.x  
**Bonus:** Django Web Application

---

## Live Website

**[Open AntiCode Rations](https://food-bank-exam-phi.vercel.app)**

The Django bonus application is deployed on Vercel and uses a Neon PostgreSQL database for persistent storage.

---

## Project Overview

This project is designed to help manage a community food bank by keeping track of registered families, available food stock, and food distribution records.

It includes two implementations:

1. **Console Application:** A Python command-line program using built-in Python features.
2. **Django Web Application (Bonus):** A browser-based interface with database-backed storage.

## Features

### Python Console Application

- Register families using unique family IDs.
- Prevent duplicate family registrations.
- Track the number of family members.
- Add food packs to available stock.
- Distribute food packs to registered families.
- Prevent distributions when stock is insufficient.
- Maintain a distribution history.
- Generate reports about families, stock, and distributions.

### Django Web Application (Bonus)

- Browser-based food bank management.
- Register and manage families.
- Add food stock.
- Distribute food packs.
- View available stock.
- View distribution history.
- Generate reports.
- Delete individual family records.
- Automatically delete associated distribution history when a family is deleted.

---

## Live Demo

Visit the deployed application:

**https://food-bank-exam-phi.vercel.app**

The website is hosted on **Vercel**, with **Neon PostgreSQL** providing the production database.

---

## How to Run

### 1. Console Application

Make sure Python 3.x is installed.

Open a terminal in the project root and run:

```bash
python main.py
```

No external packages are required for the console application.

### 2. Django Application (Bonus)

Navigate to the Django project directory:

```bash
cd "Foodbank-Django (bonus)"
```

Install Django:

```bash
pip install django
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## Project Structure

```text
Community-Food-Bank/
│
├── main.py
│
├── Foodbank-Django (bonus)/
│   │
│   ├── manage.py
│   ├── requirements.txt
│   ├── vercel.json
│   │
│   ├── foodbank/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   └── core/
│       ├── migrations/
│       ├── templates/
│       │   └── core/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── admin.py
│
└── README.md
```

---

## Classes

| Class | Description |
|---|---|
| `Family` | Stores a family's ID, name, and member count. |
| `FoodBank` | Manages stock, registers families, distributes packs, and generates reports. |

---

## Data Structures Used

| Structure | Where | Purpose |
|---|---|---|
| `dict` | `FoodBank.families` | Maps family IDs to Family objects for efficient lookup. |
| `set` | `FoodBank.registered_ids` | Tracks unique IDs and prevents duplicates. |
| `list` | `FoodBank.history` | Maintains an ordered distribution history. |
| `tuple` | Distribution history entries | Stores immutable `(family_id, packs)` records. |

---

## Django Models (Bonus)

| Model | Purpose |
|---|---|
| `Family` | Stores registered families with a unique family ID. |
| `FoodStock` | Tracks available food stock. |
| `Distribution` | Records food distributions using a ForeignKey relationship to Family. |

### Database Relationships

- Each family can have multiple distribution records.
- Each distribution belongs to one family.
- Deleting a family automatically deletes its associated distribution records through Django's `on_delete=models.CASCADE` relationship.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Main programming language |
| Django | Web application framework |
| HTML | Page structure |
| CSS | User interface styling |
| SQLite | Local development database (default Django configuration) |
| PostgreSQL | Production database |
| Neon | Managed PostgreSQL database hosting |
| Vercel | Web application deployment |
| Git | Version control |
| GitHub | Source code hosting |

---

## Deployment

The Django bonus application is deployed using Vercel.

**Deployment URL:**  
https://food-bank-exam-phi.vercel.app

**Production database:** Neon PostgreSQL

The production database connection is configured through Vercel environment variables.

Sensitive credentials such as database passwords and Django secret keys are not included in the repository.

---

## Requirements

- Python 3.x
- Django (for the bonus application)
- A web browser (for the Django application)
- Internet connection (for the deployed application)

The console application does not require external Python packages.

---

## Academic Information

**Examination:** Python Final Exam 2026  
**Project:** Community Food Bank Management System  
**Student:** ThinkShield

**Implementation:** Python Console Application + Django Web Application (Bonus)

---

## License

This project was developed as an academic examination project for educational purposes.
