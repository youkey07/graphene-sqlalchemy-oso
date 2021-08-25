from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR

from model.base import db


class ModelSchool(db.Model):
    """SCHOOL model."""

    __tablename__ = 'SCHOOL'

    school_id = Column('school_id', VARCHAR(36), primary_key=True)
    school_name = Column('school_name', VARCHAR(36), nullable=False)
