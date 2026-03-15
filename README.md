# Modular Entity and Mapping System API

This project implements a **Modular Entity and Mapping System** using Django and Django REST Framework.  
It provides CRUD APIs for master entities and their relationships using **APIView**.

The system is designed with a modular structure where entities such as vendors, products, courses, and certifications are managed separately and connected through mapping tables.

---

# Tech Stack

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger API Documentation)

---


## Master Apps:
- vendor
- product
- course
- certification

## Mapping Apps:
- vendor_product_mapping
- product_course_mapping
- course_certification_mapping

---

# Setup Steps

## 1. Clone the repository

```bash
git clone https://github.com/Kavya-N03/modular-entity-mapping-system.git
cd modular-entity-mapping-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Migration Steps

Run migrations to create database tables.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/swagger/
```

ReDoc

```
http://127.0.0.1:8000/redoc/
```

Swagger provides interactive API testing while ReDoc provides clean API documentation.

---

# API Usage Examples

## Create Vendor

POST `/vendors/`

Request Body

```json
{
  "name": "Amazon",
  "code": "AMZ",
  "description": "Global e-commerce company",
  "is_active": true
}
```

---

## Create Product

POST `/products/`

```json
{
  "name": "Laptop",
  "code": "LTP",
  "description": "Electronic device",
  "is_active": true
}
```

---

## Create Course

POST `/courses/`

```json
{
  "name": "Python Learning Kit",
  "code": "PYKIT",
  "description": "Bundle of Python learning resources",
  "is_active": true
}
```

---

## Create Certification

POST `/certifications/`

```json
{
  "name": "Python Developer Certification",
  "code": "PYCERT",
  "description": "Certification for Python developers",
  "is_active": true
}
```

---

## Create Vendor Product Mapping

POST `/vendor-product-mappings/`

```json
{
  "vendor": 1,
  "product": 1,
  "is_primary": true,
  "is_active": true
}
```

---

## Filter Vendor Product Mapping

GET

```
/vendor-product-mappings/?vendor_id=1
```

---

For the complete list of APIs and request/response schemas, refer to the Swagger documentation.