from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine

# Define SQLite database URL
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Database connection arguments
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    """
    Create all tables defined in the SQLModel metadata.
    This should be called during the project startup.
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Dependency that provides a database session.
    """
    with Session(engine) as session:
        yield session

# Dependency annotation for injecting the session
SessionDep = Annotated[Session, Depends(get_session)]
