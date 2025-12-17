from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app import schemas

router = APIRouter()

# --- Create Account ---
@router.post("/accounts/", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    db_account = models.Account(name=account.name)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

# --- Get Account ---
@router.get("/accounts/{account_id}", response_model=schemas.Account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

# --- Create Program ---
@router.post("/accounts/{account_id}/programs/", response_model=schemas.Program)
def create_program(account_id: int, program: schemas.ProgramCreate, db: Session = Depends(get_db)):
    # Check if account exists first
    db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    
    db_program = models.Program(**program.dict(), account_id=account_id)
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

# --- Get Programs (Optional Helper) ---
@router.get("/programs/{program_id}", response_model=schemas.Program)
def read_program(program_id: int, db: Session = Depends(get_db)):
    db_program = db.query(models.Program).filter(models.Program.id == program_id).first()
    if db_program is None:
        raise HTTPException(status_code=404, detail="Program not found")
    return db_program