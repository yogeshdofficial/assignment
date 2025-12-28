def test_get_banks(client):
    response = client.get("/banks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_banks_pagination(client):
    response = client.get("/banks?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert set(["total", "page", "page_size", "items"]).issubset(set(data.keys()))
    assert isinstance(data["items"], list)


def test_get_banks_invalid_pagination(client):
    # page must be >= 1 (Query validation)
    response = client.get("/banks?page=0&page_size=5")
    assert response.status_code == 422


def test_get_bank_branches(client):
    response = client.get("/banks/1/branches")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_bank_branches_pagination(client):
    response = client.get("/banks/1/branches?page=1&page_size=3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert set(["total", "page", "page_size", "items"]).issubset(set(data.keys()))
    assert isinstance(data["items"], list)
