#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.recipe import Recipe
from models.category import Category
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Recipe": Recipe, "category":Category}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('recipes_dev',
                                             'recipes_dev_pwd',
                                             'localhost',
                                             'recipes_dev_db'))
    
    def all(self, cls):
        """query on the current database session"""
        new_dict = {}
    
        objs = self.__session.query(cls).all()
        for obj in objs:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def getrecipesbytype(self,type_id):
        results = self.__session.query(Recipe).filter(Recipe.type == type_id).all()
        new_dict = {}
        for obj in results:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            new_dict[key] = obj
        return (new_dict)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

   
