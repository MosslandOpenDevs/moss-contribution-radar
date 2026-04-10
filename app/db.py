from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///moss_contribution_radar.db"
engine = create_engine(DATABASE_URL)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
