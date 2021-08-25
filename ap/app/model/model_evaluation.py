from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship

from model.base import db
from model.model_user import ModelUser
from model.model_subject import ModelSubject


class ModelEvaluation(db.Model):
    """EVALATION model."""

    __tablename__ = 'EVALUATION'

    subject_id = Column('subject_id', VARCHAR(36), ForeignKey('SUBJECT.subject_id'), primary_key=True)
    subject = relationship(ModelSubject, foreign_keys=[subject_id], lazy='bulk', backref='evaluation_list')
    evaluated_by_id = Column('evaluated_by_id', VARCHAR(36), ForeignKey('USER.user_id'), primary_key=True)
    evaluated_by = relationship(ModelUser, foreign_keys=[evaluated_by_id], lazy='bulk', backref='evaluation_list')
    evaluation = Column('evaluation', VARCHAR(36), nullable=False)
