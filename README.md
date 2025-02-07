# Job-Portal-API
A **Job Portal API** built with **Django** and **Django Ninja**. This project provides an API for managing job listings, along with a frontend interface using Django templates.

## Features

- Create, Read, and Delete job listings.
- API built using Django Ninja.
- Well-structured project with Django best practices.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/jobportal.git
cd jobportal
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations jobs
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

The project will be available at **http://127.0.0.1:8000/**

## API Endpoints

| Method | Endpoint       | Description              |
|--------|---------------|--------------------------|
| GET    | /api/jobs/    | List all job postings    |
| POST   | /api/jobs/    | Create a new job post    |
| GET    | /api/jobs/{id}/ | Get a specific job post |
| DELETE | /api/jobs/{id}/ | Delete a job post       |

## Project Structure

```
jobportal/
│── jobs/
│   ├── migrations/
│   ├── templates/jobs/
│   ├── models.py
│   ├── views.py
│   ├── api.py
│   ├── urls.py
│── jobportal/
│   ├── settings.py
│   ├── urls.py
│── manage.py
│── README.md
```

## Contribution
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.

---
**Author:** Omkar Mhaske 
**GitHub:** [OSM2030](https://github.com/OSM2030)
