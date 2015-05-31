import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Cause(Base):
	__tablename__ = 'cause'

	id = Column(Integer, primary_key = True)
	name = Column(String(100), nullable = False)

class Region(Base):
	__tablename__ = 'region'

	id = Column(Integer, primary_key = True)
	name = Column(String(100), nullable = False)

class Charity(Base):
    __tablename__ = 'charity'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    description = Column(String(150) )
    contact = Column(String(150) )
    address = Column(String(150) )
    cause_id = Column(Integer, ForeignKey('cause.id'))
    cause = relationship(Cause)
    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(Region)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    social_id = Column(String(64), nullable=False, unique=True)
    nickname = Column(String(64), nullable=False)
    email = Column(String(64), nullable=True)
    
engine = create_engine('sqlite:///charity.db')

Base.metadata.create_all(engine)  