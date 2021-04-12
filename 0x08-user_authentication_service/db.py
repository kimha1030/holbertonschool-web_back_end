#!/usr/bin/env python3
"""
Database
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB:
    """ Class DB """
    def __init__(self):
        """ Method constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Method session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method add_user that returns a User object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ Method find user that returns the first row found in the users
            table as filtered by the method's input arguments """
        usr_query = self._session.query(User).filter_by(**kwargs)
        user = usr_query.first()
        if user is None:
            raise NoResultFound
        else:
            return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Method that takes as argument a required user_id integer
            and arbitrary keyword arguments, and returns None """
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            d_user = user.__dict__
            if k in d_user:
                setattr(user, k, v)
            else:
                raise ValueError
        self._session.commit()
        return None
