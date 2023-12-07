#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of a recipe """
    
    __tablename__ = 'categories'
    name = Column(String(128), nullable=False)
    id = Column(Integer,primary_key=True,autoincrement=True)


    def __init__(self, *args, **kwargs):
        """initializes recipe"""
        super().__init__(*args, **kwargs)
