#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4

p = "HBNB_TYPE_STORAGE"
if p in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class City(BaseModel, Base):
        """ The city class for the DBstoarge """
        __tablename__ = "cities"
        name = Column(
                String(128),
                nullable=false)
        state_id = Column(
                String(60),
                nullable=false,
                ForeignKey('states.id'))

        places = relationship("Place", 
                backref="cities", 
                cascade="all,delete")

          def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)


else:
    class City(BaseModel):
        """ This class attributes remains the identify for the file storage """
        state_id = ""
        name = ""
