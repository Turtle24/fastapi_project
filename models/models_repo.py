from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    location = Column(String(255))

    weather = relationship("Weather", back_populates="user")

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, index=True)
    city: Column(String(255))
    country: Column(String(255))
    tempreture = Column(Integer)
    rain = Column(String(255))

    user = relationship('User', back_populates="weather")