# Book-Library-
Book Library with Flask and SQLite
This is a book Library flask webapp with a SQLite database.
To run the application, install the required packages using the command
                    pip install -r requirements.txt


This project is an extension of the local Book Library application. Updated with REST API Extension Features 

The system now includes a RESTful API that supports full CRUD operations. 

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


This project is an extension of the local Book Library application. It is updated with new REST API features and automated testing to make the system stable.

Added Features:

- JSON Endpoints: Created Flask `@app.route()` routes under `/api/books` that send and receive clean JSON data.
- Clear URL Parameters: Used `<int:book_id>` in the routes. This prevents endpoint conflicts and makes handling data parameters safe and simple.
- Test Coverage: Added automated tests using `pytest`. It uses an in-memory SQLite database so tests run safely in RAM without changing your real database files.
- OpenAPI 3.0 Support: Included an `openapi.yaml` file to document all API requests, responses, and validation rules.

Dependencies:

- Language: Python 3.13+
- Framework: Flask (Web framework)
- Database: Flask-SQLAlchemy (SQLite)
- Frontend: Flask-Bootstrap (Legacy layout)
- Testing: `pytest` and `pytest-cov` (For test coverage)

Running Tests:

To check that the REST API works correctly and does not break the existing frontend, activate your virtual environment and run:

pytest --cov=main --cov-report=term-missing test_api.py
