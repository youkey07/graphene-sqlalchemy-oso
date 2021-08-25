from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship

from model.base import db
from model.model_user import ModelUser
from model.model_role import ModelRole


class ModelUserRole(db.Model):
    """USER_ROLE model."""

    __tablename__ = 'USER_ROLE'

    user_id = Column('user_id', VARCHAR(36), ForeignKey('USER.user_id'), primary_key=True)
    user = relationship(ModelUser, foreign_keys=[user_id], lazy='bulk', backref='user_role_list')
    role_id = Column('role_id', VARCHAR(36), ForeignKey('ROLE.role_id'), primary_key=True)
    role = relationship(ModelRole, foreign_keys=[role_id], lazy='bulk', backref='user_role_list')
