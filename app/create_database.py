from models.base import Base
from core.database import engine, db_session
from models.user import User

Base.metadata.create_all(engine)

# Initial user
u = User(login="john", password="john", first_name="John", last_name="Doe")

db_session.add(u)
db_session.commit()
