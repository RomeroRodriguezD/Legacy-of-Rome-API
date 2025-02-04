from sqlalchemy import create_engine, Column, Integer,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class RomanModel(Base):
    __tablename__ = 'roman_chars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    year_birth = Column(Text)
    year_dead = Column(Text)
    role = Column(Text)
    curiosities = Column(Text)

# This code below was only used to create the database.

#engine = create_engine('sqlite:///roman_demo.db')
#Session = sessionmaker(bind=engine)
#session = Session()
#Base.metadata.create_all(bind=engine)
