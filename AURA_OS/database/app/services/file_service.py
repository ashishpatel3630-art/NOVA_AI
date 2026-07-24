"""File organization helpers for AURA."""

from __future__ import annotations

import os
import shutil
from pathlib import Path


class FileService:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent / "workspace"

    @classmethod
    def ensure_base_dir(cls) -> Path:
        cls.BASE_DIR.mkdir(exist_ok=True, parents=True)
        return cls.BASE_DIR

    @classmethod
    def create_folder(cls, name: str) -> Path:
        folder = cls.ensure_base_dir() / name
        folder.mkdir(exist_ok=True, parents=True)
        return folder

    @classmethod
    def rename_file(cls, source: str, target: str) -> Path:
        source_path = Path(source)
        target_path = Path(target)
        source_path.rename(target_path)
        return target_path

    @classmethod
    def move_file(cls, source: str, destination: str) -> Path:
        source_path = Path(source)
        destination_path = Path(destination)
        destination_path.parent.mkdir(exist_ok=True, parents=True)
        shutil.move(str(source_path), str(destination_path))
        return destination_path

    @classmethod
    def delete_file(cls, path: str) -> None:
        target = Path(path)
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink(missing_ok=True)

    @classmethod
    def search_files(cls, keyword: str):
        base = cls.ensure_base_dir()
        results = []
        for path in base.rglob("*"):
            if keyword.lower() in path.name.lower():
                results.append(path)
        return results

    @classmethod
    def get_file_info(cls, path: str):
        target = Path(path)
        return {
            "name": target.name,
            "exists": target.exists(),
            "is_dir": target.is_dir(),
            "size": target.stat().st_size if target.exists() else 0,
        }
