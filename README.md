## Project folder structure:
```
Api_Project_Folder/
├── API_Project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── remainder_api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── README.md
└── .gitignore
```

Remind-me-later API (Django)

This is a simple Django REST API that allows users to create reminders with a custom message, scheduled date and time, and a method of notification (SMS or Email).

## Features

- Create a reminder with:
  - Date
  - Time
  - Message
  - Reminder method: "sms" or "email"
- Stores data in a SQLite3 database

## API Endpoints
### GET /remind_new/
List all remainders.
### POST /remind_new/
Create a new reminder.

#### Sample JSON Body:
```json
{
  "date": "2025-03-23",
  "time": "23:32:23",
  "message": "Drink full bottle",
  "remind_via": "sms"
}
