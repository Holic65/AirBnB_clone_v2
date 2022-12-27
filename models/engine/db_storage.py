#!/usr/bin/python3
'''A module that defines a class to manage database storage'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """DBStorage class definition"""
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB,
                                             pool_pre_ping=True))
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ a function that queries db session depending on cls """
        classes = (User, State, City, Amenity, Place, Review)
        objects = dict()
        if cls is None:
            for class_type in classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """ a function that adds object to db """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current databse session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ a function thaht deletes obj from db session"""
        if obj is not NOne:
            self.__session.delete(obj)

    def reload(self):
        """ creates all class in dband inherit from Base"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def close(self):
        """ call remove() method on private session attribute"""
        self.__session.close()
