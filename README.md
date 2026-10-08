# Internship Management API

A backend Internship Management API built with **FastAPI, PostgreSQL, SQLAlchemy, and Alembic**. The system manages students, internships, supervisors, internship enrollment, and internship history while enforcing important business rules at the database and application levels.

## Features

* Student registration
* Unique student email
* Password validation
* Six predefined internships
* Six predefined supervisors
* Automatic supervisor assignment through internship
* Internship enrollment
* One active internship per student
* Internship duration of 30 days
* Internship completion history
* Prevention of repeating a completed internship
* Database-level constraints
* PostgreSQL triggers for internship and supervisor limits
* Alembic database migrations
* SQL negative tests for invalid states
* ER diagram and rule-to-constraint documentation

## Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Alembic**
* **Pydantic**
* **Uvicorn**

## Project Structure

```text
internship-management-api/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── db/
│   └── database.py
│
├── models/
│   ├── base.py
│   ├── student.py
│   ├── internship.py
│   ├── supervisor.py
│   └── st_in.py
│
├── schemas/
│
├── report/
│   ├── ER_diagram.png
│   └── rule_constraint_matrix.md
│
├── tests/
│
├── main.py
├── alembic.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository and move into the project directory:

```bash
git clone <repository-url>
cd internship-management-api
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and configure the PostgreSQL database connection.

Example:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost/manage_intern
```

The `.env` file is excluded from Git using `.gitignore`.

## Database Setup

Create the PostgreSQL database and configure the database connection.

The project uses **SQLAlchemy** for ORM-based database interaction and **Alembic** for schema migrations.

Run migrations with:

```bash
alembic upgrade head
```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API documentation is available through Swagger UI at:

```text
/docs
```

## Main API Endpoints

### Student Registration

```http
POST /students
```

Creates a new student.

### Internship Enrollment

```http
POST /students/{student_id}/internships/{internship_id}
```

Registers a student for an internship.

The supervisor is automatically determined from the selected internship.

### Student / Internship Data

Additional GET endpoints can be used to retrieve student and internship information.

## Business Rules

The system enforces the following core rules:

1. Student email must be unique.
2. A student can have only one active internship at a time.
3. A student cannot repeat an internship that they have already completed.
4. Every internship has one assigned supervisor.
5. A supervisor can supervise only one internship.

Some rules are enforced through PostgreSQL constraints, while others are validated in the application layer.

## Database Constraints

The database uses:

* Primary keys
* Foreign keys
* Unique constraints
* `NOT NULL` constraints
* PostgreSQL triggers

The internship and supervisor tables are restricted to six records through database triggers.

The internship-to-supervisor relationship uses a unique supervisor ID to prevent the same supervisor from being assigned to multiple internships.

## Migrations

Alembic is used for database migration management.

Create a new migration:

```bash
alembic revision --autogenerate -m "migration message"
```

Apply migrations:

```bash
alembic upgrade head
```

Rollback the latest migration:

```bash
alembic downgrade -1
```

## Testing

The project includes negative SQL tests to verify that invalid database states are rejected.

Examples include:

* Attempting to add a seventh internship
* Attempting to add a seventh supervisor
* Assigning the same supervisor to multiple internships
* Violating unique student email constraints
* Testing invalid internship enrollment states

## Documentation

The `report/` directory contains:

* `ER_diagram.png` — database entity relationship diagram
* `rule_constraint_matrix.md` — mapping between business rules and their enforcement mechanisms

## Project Status

The core database schema, business rules, constraints, migrations, seed data, ER diagram, and negative SQL tests have been implemented.

## Author

Python Backend Developer
