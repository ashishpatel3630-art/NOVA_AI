from fastapi.testclient import TestClient

from AURA_OS.database.app.api import app


def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_task_and_note():
    client = TestClient(app)

    task_response = client.post(
        "/api/tasks",
        json={"title": "Ship UI polish", "description": "Polish the new dashboard", "priority": "High", "deadline": "2026-07-24"},
    )
    note_response = client.post(
        "/api/notes",
        json={"title": "Design ideas", "category": "Planning", "content": "Capture the next sprint"},
    )

    assert task_response.status_code == 200
    assert note_response.status_code == 200
