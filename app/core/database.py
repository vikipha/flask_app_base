from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import DB_CONNECTION_STRING

engine = create_engine(DB_CONNECTION_STRING, echo=True)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)