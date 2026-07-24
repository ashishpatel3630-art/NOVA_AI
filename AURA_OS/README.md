# AURA

AURA is a Python-only personal digital operating system built with PySide6, SQLAlchemy, SQLite, Pandas, and Matplotlib.

## Features
- Dashboard with task and note metrics
- Task management
- Notes management
- File organization helpers
- Utility tools
- Settings persistence

## Run
```bash
cd AURA_OS
python3 main.py
```

## Deploy
### Desktop app bundle
```bash
cd AURA_OS
./venv/bin/pyinstaller --clean build/aura.spec
```

### Web API + frontend
1. Start the backend API:
```bash
cd AURA_OS
./venv/bin/python -m uvicorn AURA_OS.database.app.api:app --host 0.0.0.0 --port 8000
```
2. Build and serve the frontend:
```bash
cd AURA_OS/frontend
npm install
npm run build
npx serve dist
```

> Note: The desktop app is built with PySide6, while the `frontend/` folder is a separate React SPA that talks to `http://localhost:8000`.
