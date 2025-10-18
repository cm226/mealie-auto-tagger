from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.db.models.label import Base


def init_db(db_url: str):
    new_engine = create_engine(db_url, echo=not settings.production, connect_args={
        "check_same_thread": False})
    Base.metadata.create_all(new_engine)

    new_session = sessionmaker(
        autocommit=False, autoflush=False, bind=new_engine, future=True)

    return new_session, new_engine


SessionLocal, engine = init_db(settings.db_url)


def fast_api_depends_generate_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
