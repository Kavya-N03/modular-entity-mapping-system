# Modular Entity and Mapping System API

This project implements a **Modular Entity and Mapping System** using Django and Django REST Framework.  
It provides CRUD APIs for master entities and their relationships using **APIView**.

The system is designed with a modular structure where entities such as vendors, products, courses, and certifications are managed separately and connected through mapping tables.

---

## Tech Stack

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

## Setup Steps

### 1. Clone the repository

```bash
git clone https://github.com/Kavya-N03/modular-entity-mapping-system.git
cd modular-entity-mapping-system
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Migration Steps

Run migrations to create database tables.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

# API Documentation
## Live API Endpoints (Deployed on Render)

### Master APIs

**Vendors API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/vendors/

GET, POST → `/api/vendors/`  
GET, PUT, PATCH, DELETE → `/api/vendors/{id}/`

---

**Products API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/products/

GET, POST → `/api/products/`  
GET, PUT, PATCH, DELETE → `/api/products/{id}/`

---

**Courses API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/courses/

GET, POST → `/api/courses/`  
GET, PUT, PATCH, DELETE → `/api/courses/{id}/`

---

**Certifications API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/certifications/

GET, POST → `/api/certifications/`  
GET, PUT, PATCH, DELETE → `/api/certifications/{id}/`

---

### Mapping APIs

**Vendor Product Mapping API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/vendor-product-mappings/

GET, POST → `/api/vendor-product-mappings/`  
GET, PUT, PATCH, DELETE → `/api/vendor-product-mappings/{id}/`

---

**Product Course Mapping API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/product-course-mappings/

GET, POST → `/api/product-course-mappings/`  
GET, PUT, PATCH, DELETE → `/api/product-course-mappings/{id}/`

---

**Course Certification Mapping API**  
🔗 https://modular-entity-mapping-system.onrender.com/api/course-certification-mappings/

GET, POST → `/api/course-certification-mappings/`  
GET, PUT, PATCH, DELETE → `/api/course-certification-mappings/{id}/`


### Filtering APIs

**Filtering by `vendor_id`, `product_id`, `course_id`**

🔗 https://modular-entity-mapping-system.onrender.com/api/vendor-product-mappings/?vendor_id={id}

🔗 https://modular-entity-mapping-system.onrender.com/api/product-course-mappings/?product_id={id}

🔗 https://modular-entity-mapping-system.onrender.com/api/course-certification-mappings/?course_id={id}

---

### Admin Panel

🔗 https://modular-entity-mapping-system.onrender.com/admin/

**Username:** admin  
**Password:** admin123

🔗 **Swagger UI**  
https://modular-entity-mapping-system.onrender.com/swagger/

🔗 **ReDoc Documentation**  
https://modular-entity-mapping-system.onrender.com/redoc/

Swagger provides interactive API testing while ReDoc provides clean API documentation.

---

## Postman Collections

[Open Postman Collection](https://www.postman.com/docking-module-physicist-25504295/workspace/public-workspace/collection/44863223-528b641e-c59e-432a-b849-e384250309b9?action=share&source=copy-link&creator=44863223)


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