def test_get_posts(base_url, session, timeout):
    response = session.get(f"{base_url}/posts", timeout=timeout)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "userId" in data[0]
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]


def test_get_single_post(base_url, session, timeout):
    response = session.get(f"{base_url}/posts/1", timeout=timeout)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "userId" in data
    assert "title" in data
    assert "body" in data


def test_create_post(base_url, session, timeout):
    payload = {
        "title": "Jahnavi",
        "body": "Software Tester",
        "userId": 1
    }

    response = session.post(f"{base_url}/posts", json=payload, timeout=timeout)
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_update_post(base_url, session, timeout):
    payload = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = session.put(f"{base_url}/posts/1", json=payload, timeout=timeout)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == 1


def test_delete_post(base_url, session, timeout):
    response = session.delete(f"{base_url}/posts/1", timeout=timeout)
    assert response.status_code == 200


def test_get_invalid_post(base_url, session, timeout):
    response = session.get(f"{base_url}/posts/999999", timeout=timeout)
    assert response.status_code == 404 or response.json() == {}

def test_create_post_invalid_payload(base_url, session, timeout):
    payload = {
        "title": "",
        "body": "",
        "userId": None
    }

    response = session.post(f"{base_url}/posts", json=payload, timeout=timeout)

    assert response.status_code in [201, 400]

    data = response.json()
    assert "id" in data