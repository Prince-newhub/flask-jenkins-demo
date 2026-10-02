from app import app

client=app.test_client()
reponse=client.get("/")

assert response.status_code == 200
assert response.data == b"Hello from Flask CI/CD"