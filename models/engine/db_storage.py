#!/usr/bin/python3
"""This module defines the DBStorage engine for the HBNB project using SQLAlchemy"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Database Storage Engine using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage engine"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{db}',
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects or all objects of a given class from the current session"""
        obj_dict = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session().query(cls)
            for obj in query:
                key = f"{type(obj).__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            for cls in classes:
                query = self.__session().query(cls)
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add a new object to the current session"""
        self.__session().add(obj)

    def save(self):
        """Commit all changes of the current session"""
        self.__session().commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""
        if obj:
            self.__session().delete(obj)

    def reload(self):
        """Create all tables and initialize the session"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def close(self):
        """Remove the current SQLAlchemy session"""
        self.__session.remove()
