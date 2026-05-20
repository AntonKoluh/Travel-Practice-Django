# Django REST API Project

A small Django + Django REST Framework API for managing projects and place visits.  
The API uses token authentication, versioned routes, pagination, filtering, search, ordering, and restricted partial updates.

## Tech Stack

- Python
- Django
- Django REST Framework
- DRF Token Authentication
- django-filter
- SQLite by default

## Main Features

- Token-based authentication
- Admin-protected API endpoints
- Versioned API prefix: `/api/v1/`
- CRUD endpoints using DRF `ModelViewSet`
- Pagination support
- Query filtering with `django-filter`
- Search and ordering support
- Restricted `PATCH` updates for visit fields such as `note` and `is_visited`
- Check place_id against external API `https://api.artic.edu/api/v1/artworks/...`

## Clone Repo

```bash
git clone https://github.com/AntonKoluh/Travel-Practice-Django.git
cd Travel-Practice-Django
```

## Run with docker compose

```bash
docker compose up -d --build
```

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

## Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Run the Server

```bash
python manage.py runserver
```

Default local URL:

```txt
http://127.0.0.1:8000/
```

## Authentication

Get an auth token:

```http
POST /api-token-auth/
```

Example body:

```json
{
  "username": "admin",
  "password": "your_password"
}
```

Use the token in requests:

```http
Authorization: Token your_token_here
Content-Type: application/json
```

## API Routes

Example routes:

```txt
/api/v1/users/
/api/v1/projects/
/api/v1/places/
```

Detail routes:

```txt
/api/v1/projects/<id>/
/api/v1/places/<id>/
```

## Filtering, Search, Ordering, and Pagination

Example query params:

```txt
/api/v1/places/?project_id=1
/api/v1/places/?is_visited=true
/api/v1/places/?search=park
/api/v1/places/?ordering=-id
/api/v1/places/?page=2
```

## PATCH Restrictions

The visit endpoint only allows partial updates for selected fields:

```json
{
  "note": "Visited yesterday",
  "is_visited": true
}
```

Fields outside the allowed list are rejected.

## Common Notes

Make sure JSON requests are sent with:

```http
Content-Type: application/json
```

In Postman, use:

```txt
Body -> raw -> JSON
```

Otherwise DRF may return:

```json
{
  "detail": "Unsupported media type \"text/plain\" in request."
}
```

## Development Checklist

- Run migrations after model changes
- Create a superuser for admin access
- Use `Authorization: Token <token>` for protected endpoints
- Keep API URLs under `/api/v1/`
- Use serializers for validation and ViewSets for endpoint logic
