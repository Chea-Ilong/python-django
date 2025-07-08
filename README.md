# Django URL Configuration

**Date:** July 6, 2025

This document outlines the URL routing configuration for a Django application with three main modules:

- `/auth/` – Handles authentication and user-related actions  
- `/site_setting/` – Manages site content such as pricing plans, icons, team members, and invitation templates  
- `/events/` – Handles CRUD operations for event management  

---

## 1. Authentication Routes (`/auth/`)

These routes are defined in the authentication app.

### Signup  
- `POST /auth/signup/`

### Login / Logout  
- `POST /auth/login/`  
- `POST /auth/logout/`

### Profile  
- `GET /auth/profile/`

### Password Management  
- `POST /auth/password/change/`  
- `POST /auth/password/reset/`  
- `POST /auth/password/reset/confirm/<uidb64>/<token>/`

### JWT Token Handling  
- `POST /auth/token/verify/`  
- `POST /auth/token/refresh/`

### Google Social Auth  
- `GET /auth/google/`

---

## 2. Site Settings Routes (`/site_setting/`)

These endpoints are generated using Django REST Framework routers and handle content management.

### Registered ViewSets  
- `GET / POST /site_setting/pricing-plans/`  
- `GET / POST /site_setting/icons/`  
- `GET / POST /site_setting/team-members/`  
- `GET / POST /site_setting/invitation-templates/`

---

## 3. Event Management Routes (`/events/`)

Event-related endpoints provided by a DRF ViewSet.

- `GET / POST /events/`  
- `GET / PUT / DELETE /events/<id>/`

---

## 4. Conclusion

This configuration provides a clear and modular API structure, with separate routes for:

- User authentication and authorization  
- Site content management via DRF routers  
- Full CRUD support for event handling  
