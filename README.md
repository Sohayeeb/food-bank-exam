# Community Food Bank — Python Final Exam 2026

**Student:** ThinkShield

---

## How to Run

### Console App (main.py)

```bash
python main.py
```

No external packages required. Python 3.x only.

### Django App (Bonus)

```bash
cd Foodbank-Django (bonus)
pip install django
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

---

## Classes

| Class | Description |
|---|---|
| `Family` | Stores a family's ID, name, and member count |
| `FoodBank` | Manages stock, registers families, distributes packs, and generates reports |

---

## Data Structures Used

| Structure | Where |
|---|---|
| `dict` | `FoodBank.families` — maps family ID → Family object for O(1) lookup |
| `set` | `FoodBank.registered_ids` — tracks unique IDs, prevents duplicates |
| `list` | `FoodBank.history` — ordered log of all distributions |
| `tuple` | Each history entry is `(family_id, packs)` — immutable record |

---

## Django Models (Bonus)

| Model | Purpose |
|---|---|
| `Family` | Registered families with unique ID constraint |
| `FoodStock` | Single-row stock tracker |
| `Distribution` | FK to Family; records every distribution event |
