# Legal RAG - Frontend (Vite + React + TypeScript + Tailwind)

This is a ready-to-run frontend designed to work with your existing FastAPI backend.

## How to run

1. Install Node (recommend Node 18+; Node 20+ is preferred).
2. From this folder run:
   ```bash
   npm install
   npm run dev
   ```
3. Open the site at http://localhost:5173

## Environment
Create a `.env` file (in the project root) with:
```
VITE_API_URL=http://127.0.0.1:8000
```
Change it if your backend runs elsewhere.

## Notes
- This frontend expects backend routes:
  - POST /auth/register
  - POST /auth/login
  - POST /create-session?user_id=...
  - POST /upload (form-data user_id, session_id, file)
  - GET /list-files?user_id=...&session_id=...
  - POST /chat (form-data user_id, session_id, message)
- Session id is stored in `sessionStorage` and is not printed in the UI.

