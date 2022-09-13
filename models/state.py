#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Gets a list of all related City objects."""
            all_cities = list(models.storage.all("City").values())
            temp = []
            for c_id in all_cities:
                if all_cities[c_id].state_id == self.id:
                    temp.append(all_cities[c_id])
            return temp
