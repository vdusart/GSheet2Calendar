from sqlalchemy import Column, String, Integer

from utils.base import Base


class Timetables(Base):
    __tablename__ = 'timetables'

    id = Column(Integer, primary_key=True)
    gid = Column('gid', String(20))
    name = Column('name', String(20))
    spreadsheet_id = Column('spreadsheet_id', String(50))
