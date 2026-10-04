Little Lemon Restaurant Booking API
===================================

This project provides a Django-served static landing page, menu API, and authenticated CRUD booking endpoints using Django REST Framework.
MySQL is configured by default; set USE_SQLITE=true for a zero-config local demo.

Quick start
1. Create and activate a virtual environment.
2. pip install -r requirements.txt
3. Configure MySQL (variables below), then run python manage.py migrate
4. python manage.py runserver

MySQL environment variables: MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT.

API paths for peer review / Insomnia
GET /api/menu-items/
POST /api/menu-items/
GET /api/menu-items/<id>/
PUT /api/menu-items/<id>/
DELETE /api/menu-items/<id>/
POST /api/registration/
  JSON: {"username":"ada","email":"ada@example.com","password":"secure-pass-123"}
  Returns a token.
GET /api/bookings/
POST /api/bookings/
  JSON: {"name":"Ada Lovelace","no_of_guests":2,"booking_date":"2026-10-10T18:30:00Z"}
GET /api/bookings/<id>/
PUT /api/bookings/<id>/
DELETE /api/bookings/<id>/

POST /api-token-auth/ (Django REST Framework token endpoint)
User registration/login endpoints: /auth/users/ and /auth/token/login/ (Djoser)

For booking endpoints set: Authorization: Token <token returned by registration>
Run tests locally: USE_SQLITE=true python manage.py test
