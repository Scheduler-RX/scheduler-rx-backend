## Project: SchedulerRX (SaaS Residency Scheduler)
**Goal:** MVP Demo by Tuesday.
**Stack:**
- Frontend: React + Vite + Tailwind (Port 5173)
- Backend: FastAPI + Python (Port 8000)
- Auth: Clerk (React SDK)
- Database: Postgres (Docker Container on Port 5432)
- ORM: SQLAlchemy + Alembic

**Current Status:**
- Frontend and Backend are in separate repos.
- Auth (Clerk) is working and protecting the Dashboard.
- Backend (FastAPI) is running and CORS is configured.
- Database (Docker) is running.
- Backend connected to DB via DATABASE_URL.

**Immediate Next Task:**
- Issue 1.6: Database Schema Migration (Alembic).