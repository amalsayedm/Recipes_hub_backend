#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship


class Favorites(BaseModel, Base):
    """Representation of a user """
    
    __tablename__ = 'favorites'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'), nullable=False)
    recipe_id = Column(Integer,ForeignKey('recipes.id'), nullable=False)
    user_relation = relationship("User", backref="favorites")
    recipe_relation = relationship("Recipe", backref="favorites")

    def __init__(self, *args, **kwargs):
        """initializes """
        super().__init__(*args, **kwargs)

   

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
