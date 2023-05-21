# Felp: Restaurant Viewer Backend Application

This repository contains the backend application for a restaurant viewer using FastAPI. The application provides an API for retrieving information about various restaurants, including their menus, locations, and reviews.

## Installation

To run the backend application locally, follow these steps:

1. Clone the repository:


2. Navigate to the project directory:


3. Create a virtual environment:
```
python -m venv venv
```

4. Activate the virtual environment:

- **Windows**:

  ```
  venv\Scripts\activate
  ```

- **Linux/Mac**:

  ```
  source venv/bin/activate
  ```

5. Install the dependencies:
```
pip install -r requirements.txt
```

6. Set up the database:

- The application uses a PostgreSQL database. Make sure you have PostgreSQL installed and running.

- Create a new database for the application.

- Update the database connection details in the `.env` file located in the project's root directory.

7. Run the database migrations:
```
alembic upgrade head

```


8. Start the FastAPI server:
```
uvicorn app.main:app --reload

```

The server should now be running at `http://localhost:8000`.

## API Documentation

The API documentation is automatically generated by FastAPI and can be accessed at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.



