#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Recipe(BaseModel, Base):
    """Representation of a recipe """
    
    __tablename__ = 'recipes'
    name = Column(String(128), nullable=False)
    total_time = Column(String(128), nullable=False)
    images = Column(String(400), nullable=False)
    link = Column(String(400), nullable=False)
    rating = Column(Float, nullable=False)
    type = Column(Integer,ForeignKey('categories.id'), nullable=False)
    Catrgory_relation = relationship("Category", backref="recipes")
    id = Column(Integer,primary_key=True,autoincrement=True)


    def __init__(self, *args, **kwargs):
        """initializes recipe"""
        super().__init__(*args, **kwargs)
