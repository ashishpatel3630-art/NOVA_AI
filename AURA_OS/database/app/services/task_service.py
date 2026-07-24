"""Task business logic for AURA."""

from AURA_OS.database.app.database.session import get_session
from AURA_OS.database.app.models.task import Task


class TaskService:
    @staticmethod
    def get_tasks():
        session = get_session()
        try:
            return session.query(Task).order_by(Task.id.desc()).all()
        finally:
            session.close()

    @staticmethod
    def create_task(title: str, description: str, priority: str, deadline: str):
        session = get_session()
        try:
            task = Task(
                title=title,
                description=description,
                priority=priority,
                deadline=deadline,
                status="Pending",
            )
            session.add(task)
            session.commit()
            return task
        finally:
            session.close()

    @staticmethod
    def delete_task(task_id: int):
        session = get_session()
        try:
            task = session.get(Task, task_id)
            if task is not None:
                session.delete(task)
                session.commit()
            return task
        finally:
            session.close()

    @staticmethod
    def search_task(keyword: str):
        session = get_session()
        try:
            if not keyword:
                return TaskService.get_tasks()
            pattern = f"%{keyword}%"
            return (
                session.query(Task)
                .filter(Task.title.like(pattern))
                .order_by(Task.id.desc())
                .all()
            )
        finally:
            session.close()

    @staticmethod
    def get_total_tasks() -> int:
        session = get_session()
        try:
            return session.query(Task).count()
        finally:
            session.close()

    @staticmethod
    def get_completed_tasks() -> int:
        session = get_session()
        try:
            return session.query(Task).filter(Task.status == "Completed").count()
        finally:
            session.close()

    @staticmethod
    def get_pending_tasks() -> int:
        session = get_session()
        try:
            return session.query(Task).filter(Task.status == "Pending").count()
        finally:
            session.close()