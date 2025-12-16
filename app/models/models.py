from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum as SqlEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    PROGRAM_ADMIN = "program_admin"
    RESIDENT = "resident"

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    programs = relationship("Program", back_populates="account")

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
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