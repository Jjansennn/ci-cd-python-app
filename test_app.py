import app


def test_home():
    assert app.home() == "Hello CI/CD with Python!"