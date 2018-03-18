from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True)
Session = sessionmaker(bind=engine)
