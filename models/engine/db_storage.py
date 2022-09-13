#!/usr/bin/python3
""" This is the DBStoarge class for HBNB project"""

from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from models import *

class DBStorage:
    __engine = None
    __session = None
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        self.__engine = create_engine('mysql://' + 
                environ['HBNB_MYSQL_USER'] + ':' + 
                environ['HBNB_MYSQL_PWD'] + '@' + 
                environ['HBNB_MYSQL_HOST'] + ':3306/' + 
                environ['HBNB_MYSQL_DB'],
                pool_pre_ping=True)

        try:
            if environ['HBNB_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        storage = {}
        if cls is None:
            for cls_name in self.classes:
                for instance in self.__session.query(eval(cls_name)):
                    storage[instance.id] = instance
        else:
            if cls not in self.classes:
                return
            for instance in self.__session.query(eval(cls)):
                storage[instance.id] = instance

        return storage
     def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise
        finally:
            self.__session.close()

    def update(self, cls, obj_id, key, new_value):
        res = self.__session.query(eval(cls)).filter(eval(cls).id == obj_id)

        if res.count() == 0:
            return 0

        res.update({key: (new_value)})
        return 1

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def delete(self, obj=None):
        if obj is None:
            return False
        self.__session.delete(obj)

    def close(self):
        self.__session.reload()

    def close(self):
        self.__session.remove()
