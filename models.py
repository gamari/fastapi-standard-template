from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()
metadata = MetaData()

class Todo(Base):
    __tablename__ = "todo"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)