# Book-Library-
Book Library with Flask and SQLite
This is a book Library flask webapp with a SQLite database.
To run the application, install the required packages using the command
                    pip install -r requirements.txt


Updated with REST API Extension Features 

The system now includes a RESTful API that supports full CRUD operations. This allows the backend to handle data separately from the HTML frontend.

Added Features:

- JSON Endpoints: Created Flask @app.route() endpoints that send and receive clean JSON data.
- Clear URL Parameters: Used <int:book_id> in routes to avoid conflicts and make parameter handling simple and safe.
- Test Coverage: Added automated tests using pytest with an in-memory SQLite database to ensure all API functions work correctly.
- OpenAPI 3.0 Support: Included an openapi.yaml file to document API requests, responses, and validation rules.

Dependencies:

- Language: Python 3.13+
- Framework: Flask
- Database: Flask-SQLAlchemy (SQLite)
- Frontend: Flask-Bootstrap (Legacy)
- Testing: pytest, pytest-cov

Running Tests

To check that the REST API works correctly and does not break the existing frontend, activate your virtual environment and run:

pytest --cov=main --cov-report=term-missing test_api.py
