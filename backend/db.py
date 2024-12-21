from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase  


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres/postgres')
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase): 
    pass