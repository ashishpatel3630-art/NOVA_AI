from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from AURA_OS.database.app.core.config import Config
from AURA_OS.database.app.core.database import initialize_database
from AURA_OS.database.app.services.note_service import NoteService
from AURA_OS.database.app.services.task_service import TaskService
from AURA_OS.database.app.services.file_service import FileService

initialize_database()

app = FastAPI(title="AURA API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok", "app": Config.APP_NAME}


@app.get("/api/dashboard")
def dashboard():
    return {
        "tasks": TaskService.get_total_tasks(),
        "completed": TaskService.get_completed_tasks(),
        "pending": TaskService.get_pending_tasks(),
        "notes": NoteService.get_total_notes(),
        "recent_tasks": [
            {
                "title": task.title,
                "priority": task.priority,
                "deadline": task.deadline or "No deadline",
                "status": task.status,
            }
            for task in TaskService.get_tasks()[:3]
        ],
    }


@app.get("/api/tasks")
def get_tasks():
    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "deadline": task.deadline,
        }
        for task in TaskService.get_tasks()
    ]


@app.post("/api/tasks")
def create_task(payload: dict):
    task = TaskService.create_task(
        payload.get("title", ""),
        payload.get("description", ""),
        payload.get("priority", "Medium"),
        payload.get("deadline", ""),
    )
    return {"id": task.id, "title": task.title}


@app.get("/api/notes")
def get_notes():
    return [
        {
            "id": note.id,
            "title": note.title,
            "category": note.category,
            "content": note.content,
        }
        for note in NoteService.get_notes()
    ]


@app.post("/api/notes")
def create_note(payload: dict):
    note = NoteService.create_note(
        payload.get("title", "Untitled"),
        payload.get("category", "General"),
        payload.get("content", ""),
    )
    return {"id": note.id, "title": note.title}


@app.get("/api/files")
def get_files():
    base = FileService.ensure_base_dir()
    results = []
    for path in sorted(base.rglob("*")):
        if path.name.startswith("."):
            continue
        results.append(
            {
                "name": path.name,
                "path": str(path),
                "is_dir": path.is_dir(),
                "size": path.stat().st_size if path.exists() else 0,
            }
        )
    return results
