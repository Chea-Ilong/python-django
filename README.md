
# Django Authentication Project

This is a Django-based web application designed to handle user authentication and related functionality.

## Features

- User registration and login
- Token-based authentication using JWT
- Profile view and update
- Password reset and change
- Modular Django app structure

## Project Structure

```
revise/
└── myproject/
    ├── manage.py
    ├── db.sqlite3
    ├── requirements.txt
    ├── authentications/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── urls.py
    │   ├── views.py
    │   └── ...
```

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repo-url>
    cd myproject
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

## 🧠 API Endpoints

### 🔐 Authentication

| Method | Endpoint                       | Description                       | Auth Required  |
|--------|--------------------------------|-----------------------------------|----------------|
| POST   | `/api/signup/`                 | Register a new user               | ❌ No          |
| POST   | `/api/login/`                  | Log in and obtain token           | ❌ No          |
| POST   | `/api/logout/`                 | Log out the current user          | ✅ Yes         |

### 👤 User Profile

| Method | Endpoint            | Description                      | Auth Required |
|--------|---------------------|----------------------------------|----------------|
| GET    | `/api/profile/`     | Get current user's profile       | ✅ Yes         |
| PUT    | `/api/profile/`     | Update current user's profile    | ✅ Yes         |
| PATCH  | `/api/profile/`     | Partially update user profile    | ✅ Yes         |

### 🔑 Password Management

| Method | Endpoint                               | Description                                | Auth Required |
|--------|----------------------------------------|--------------------------------------------|----------------|
| POST   | `/api/password/change/`                | Change the current password                | ✅ Yes         |
| POST   | `/api/password/reset/`                 | Send password reset email                  | ❌ No          |
| POST   | `/api/password/reset/confirm/<uidb64>/<token>/` | Confirm password reset with token   | ❌ No          |

### 🔁 JWT Token

| Method | Endpoint          | Description                    | Auth Required |
|--------|-------------------|--------------------------------|----------------|
| POST   | `/api/token/verify/` | Verify validity of token     | ✅ Yes         |

## Requirements

- Python 3.8+
- Django 3.2+ or 4.x
- Django REST Framework
- dj-rest-auth
- djangorestframework-simplejwt

## License

This project is licensed under the MIT License.
