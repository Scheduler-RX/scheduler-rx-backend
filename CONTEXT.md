## Project: SchedulerRX (SaaS Residency Scheduler)
**Goal:** MVP Demo by Tuesday.
**Stack:**
- Frontend: React + Vite + Tailwind (Port 5173)
- Backend: FastAPI + Python (Port 8000)
- Auth: Clerk (React SDK on Frontend; Backend integration pending)
- Database: Postgres (Docker Container on Port 5432)
- ORM: SQLAlchemy + Alembic

**Current Status (As of Dec 18):**
- **Repo Structure:** Currently separate repos (`scheduler-rx-frontend`, `scheduler-rx-backend`), but scheduled for Monorepo migration.
- **Feature Complete:** Account Setup Flow (Issue 2.1) is DONE.
    - UI Wizard works (Create Org -> Create Program -> Review).
    - Backend creates `Account` and `Program` correctly.
    - `ProgramAdmin` table links the creator to the program (currently using placeholder `user_id=1`).
- **Database:**
    - Models updated with `Program` sizing fields (residents, years, blocks).
    - `Account` names are now unique.
    - `ProgramAdmin` join table exists.

**Known Technical Debt (To Fix Post-Monorepo):**
- Frontend: Account ID caching bug on retry & `NaN` validation for numeric fields.
- Backend: `create_program` uses non-atomic transactions (should be one commit).
- Backend: Hardcoded `user_id=1` in `admin.py` (needs Clerk integration).

**Immediate Next Tasks:**
1. **[PRIORITY]** Migration: Convert to Monorepo structure (New Issue).
2. Cleanup: Fix bugs identified by Cursor during Issue 2.1 merge (New Sub-issue).
3. Feature: Backend Auth Integration (Prerequisite for Issue 2.2).