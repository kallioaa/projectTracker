from routes import index


def test_index():
    assert index() == "Hello World"
