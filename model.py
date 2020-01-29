from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()




class Users(Base):
	__tablename__ = 'gamers'
	gamer_id = Column(Integer,primary_key =True)
	Gmail = Column(String)
	name = Column(String)
	password = Column(String)