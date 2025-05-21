#!/usr/bin/python3
"""Base model module.

This module defines a base class for all models in our hbnb clone
"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models."""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiate a new model."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v,
                                                       '%Y-%m-%dT%H:%M:%S.%f'))
                elif k != '__class__':
                    setattr(self, k, v)

    def __str__(self):
        """Return a string representation of the instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        filtered_dict = {
                         k: v for k, v in self.__dict__.copy().items()
                         if k != '_sa_instance_state'
                         }
        return '[{}] ({}) {}'.format(cls, self.id, filtered_dict)

    def save(self):
        """Update updated_at with current time when instance is changed."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format."""
        dictionary = self.__dict__.copy()

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)
