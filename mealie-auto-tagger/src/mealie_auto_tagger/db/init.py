
from typing import Generator
from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.db.models.label import Base
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

def initDB(db_url: str):
    engine = create_engine(db_url, echo=not settings.production, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

    return SessionLocal, engine

SessionLocal, engine = initDB(settings.db_url)

def fast_API_depends_generate_session() -> Generator[Session, None, None]:
    global SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()