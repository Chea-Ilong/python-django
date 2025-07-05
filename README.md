## 🚀 Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Chea-Ilong/python-django/
    cd myproject
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **On Linux/macOS**:
      ```bash
      source venv/bin/activate 
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

---

## 🧠 API Endpoints

### 🔐 Authentication

| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| POST   | `/api/signup/`      | Register a new user               |
| POST   | `/api/login/`       | Log in and obtain token           |
| POST   | `/api/logout/`      | Log out the current user          |

### 👤 User Profile

| Method | Endpoint        | Description                      |
|--------|-----------------|----------------------------------|
| GET    | `/api/profile/` | Get current user's profile       |
| PUT    | `/api/profile/` | Update current user's profile    |
| PATCH  | `/api/profile/` | Partially update user profile    |

### 🔑 Password Management

| Method | Endpoint                                        | Description                                |
|--------|-------------------------------------------------|--------------------------------------------|
| POST   | `/api/password/change/`                         | Change the current password                |
| POST   | `/api/password/reset/`                          | Send password reset email                  |
| POST   | `/api/password/reset/confirm/<uidb64>/<token>/` | Confirm password reset with token          | 

### 🔁 JWT Token

| Method | Endpoint             | Description                    |
|--------|----------------------|--------------------------------|
| POST   | `/api/token/verify/` | Verify validity of token       |

---

## 📦 Requirements

- Python 3.10+
- Django 5.x
- Django REST Framework
- dj-rest-auth
- djangorestframework-simplejwt

---

## 📜 License

This project is licensed under the MIT License.
