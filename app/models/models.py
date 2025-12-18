from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum as SqlEnum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    PROGRAM_ADMIN = "program_admin"
    RESIDENT = "resident"

class ProgramAdmin(Base):
    __tablename__ = "program_admins"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    program_id = Column(Integer, ForeignKey("programs.id"))

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    programs = relationship("Program", back_populates="account")

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    num_residents_per_class = Column(Integer, default=10)
    program_length_years = Column(Integer, default=3)
    blocks_per_year = Column(Integer, default=13)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = relationship("Account", back_populates="programs")
    users = relationship("User", back_populates="program")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    role = Column(SqlEnum(UserRole), default=UserRole.RESIDENT)
    program_id = Column(Integer, ForeignKey("programs.id"))
    program = relationship("Program", back_populates="users")
    time_off_requests = relationship("TimeOffRequest", back_populates="user")

class TimeOffRequest(Base):
    __tablename__ = "time_off_requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default="pending")
    user = relationship("User", back_populates="time_off_requests")