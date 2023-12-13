#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    
    __tablename__ = 'users'
    device_id = Column(String(128), nullable=False)
    id = Column(Integer,primary_key=True,autoincrement=True)
   

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
