import pytest
from main import app, db, Book

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_create_book_success(client):
    payload = {"title": "The Hobbit", "author": "J.R.R. Tolkien", "rating": 9.5}
    response = client.post('/api/books', json=payload)
    assert response.status_code == 201
    assert response.json['title'] == "The Hobbit"

def test_get_all_books(client):
    client.post('/api/books', json={"title": "Book 1", "author": "Author 1", "rating": 8.0})
    response = client.get('/api/books')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_single_book_success(client):
    client.post('/api/books', json={"title": "Book 1", "author": "Author 1", "rating": 8.0})
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert response.json['title'] == "Book 1"

def test_update_book_success(client):
    client.post('/api/books', json={"title": "Old Title", "author": "Author", "rating": 5.0})
    update_payload = {"title": "New Title", "author": "Author", "rating": 9.0}
    response = client.put('/api/books/1', json=update_payload)
    assert response.status_code == 200
    assert response.json['title'] == "New Title"

def test_delete_book_success(client):
    client.post('/api/books', json={"title": "To Delete", "author": "Author", "rating": 1.0})
    response = client.delete('/api/books/1')
    assert response.status_code == 200
    assert response.json['message'] == "Deleted"

def test_create_book_missing_fields(client):
    payload = {"title": "Incomplete Book"}
    response = client.post('/api/books', json=payload)
    assert response.status_code == 400

def test_create_duplicate_book_title(client):
    payload = {"title": "Unique Book", "author": "Author", "rating": 7.0}
    client.post('/api/books', json=payload)
    response = client.post('/api/books', json=payload)
    assert response.status_code == 400

def test_get_book_not_found(client):
    response = client.get('/api/books/999')
    assert response.status_code == 404

def test_update_book_not_found(client):
    response = client.put('/api/books/999', json={"title": "Ghost", "author": "Ghost", "rating": 1.0})
    assert response.status_code == 404

def test_update_book_duplicate_title(client):
    client.post('/api/books', json={"title": "Book A", "author": "Author", "rating": 5.0})
    client.post('/api/books', json={"title": "Book B", "author": "Author", "rating": 6.0})
    response = client.put('/api/books/2', json={"title": "Book A"})
    assert response.status_code == 400

def test_delete_book_not_found(client):
    response = client.delete('/api/books/999')
    assert response.status_code == 404