#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class for a MySQL database"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns list of City instances with state_id equal to State.id"""
            city_instance_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_instance_list.append(city)
            return city_instance_list
