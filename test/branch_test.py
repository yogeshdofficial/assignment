def test_invalid_ifsc(client):
    response = client.get("/branches/INVALID000")
    assert response.status_code == 404


def test_branches_invalid_pagination(client):
    response = client.get("/banks/1/branches?page=0&page_size=5")
    assert response.status_code == 422
