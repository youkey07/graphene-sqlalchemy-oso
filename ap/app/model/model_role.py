from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR

from model.base import db


class ModelRole(db.Model):
    """ROLE model."""

    __tablename__ = 'ROLE'

    role_id = Column('role_id', VARCHAR(36), primary_key=True)
    role_name = Column('role_name', VARCHAR(36), nullable=False)
