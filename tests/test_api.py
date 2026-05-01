import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Test 1: Get list of posts - should return 200
def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "title" in data[0]
    assert "id" in data[0]
    print("✅ Get posts passed!")

# Test 2: Get single post - should return 200
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    print("✅ Get single post passed!")

# Test 3: Create a new post - should return 201
def test_create_post():
    payload = {"title": "Jahnavi", "body": "Software Tester", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Jahnavi"
    assert data["body"] == "Software Tester"
    assert "id" in data
    print("✅ Create post passed!")

# Test 4: Update a post - should return 200
def test_update_post():
    payload = {"title": "Updated Title", "body": "Updated Body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["body"] == "Updated Body"
    print("✅ Update post passed!")

# Test 5: Delete a post - should return 200
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    print("✅ Delete post passed!")

# Test 6: Get non-existent post - should return 404
def test_get_invalid_post():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404
    print("✅ Negative test passed!")