from pydantic import BaseModel
from typing import List, Optional

# --- Programs ---
class ProgramBase(BaseModel):
    name: str
    num_residents_per_class: int = 10
    program_length_years: int = 3
    blocks_per_year: int = 13

class ProgramCreate(ProgramBase):
    pass

class Program(ProgramBase):
    id: int
    account_id: int

    class Config:
        from_attributes = True # This tells Pydantic to read SQLAlchemy models

# --- Accounts ---
class AccountBase(BaseModel):
    name: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    programs: List[Program] = []

    class Config:
        from_attributes = True