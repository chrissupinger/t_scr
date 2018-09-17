from sqlalchemy import create_engine, Float, ForeignKey, Column, Date, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

_db = create_engine('sqlite:///_db.db', echo = False)
_Base = declarative_base()

class t_db(_Base):

    __tablename__ = 't_db'

    _id = Column(String, primary_key = True, nullable = True)
    _origin = Column(String, primary_key = True, nullable = False)
    _fullname = Column(String)
    _username = Column(String)
    _timestamp = Column(DateTime)
    _tweet = Column(String)

    def __init__(self, _id, _origin, _fullname, _username, _timestamp, _tweet):

        self._id = _id
        self._origin = _origin
        self._fullname = _fullname
        self._username = _username
        self._timestamp = _timestamp
        self._tweet = _tweet


_Base.metadata.create_all(_db)
