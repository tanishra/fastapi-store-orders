from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker

# SQLite database URL
DATABASE_URL = "sqlite:///store.db"

# Create SQLModel engine
engine = create_engine(DATABASE_URL, echo=True)

# ---- SQLModel Methods ----
def init_db():
    """Create all tables for SQLModel models."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency to get a SQLModel session."""
    with Session(engine) as session:
        yield session

# ---- SQLAlchemy-compatible Methods ----
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get a SQLAlchemy session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
