from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, VARCHAR
from sqlalchemy.orm import relationship

from model.base import db
from model.model_user import ModelUser


class ModelReportCard(db.Model):
    """REPORT_CARD model."""

    __tablename__ = 'REPORT_CARD'

    report_card_id = Column('report_card_id', VARCHAR(36), primary_key=True)
    user_id = Column('user_id', VARCHAR(36), ForeignKey('USER.user_id'), nullable=False)
    user = relationship(ModelUser, foreign_keys=[user_id], lazy='bulk', backref='my_report_card')
    first_evaluator_id = Column('first_evaluator_id', VARCHAR(36), ForeignKey('USER.user_id'), nullable=False)
    first_evaluator = relationship(ModelUser, foreign_keys=[first_evaluator_id], lazy='bulk', backref='first_evaluate_card_list')
    second_evaluator_id = Column('second_evaluator_id', VARCHAR(36), ForeignKey('USER.user_id'), nullable=False)
    second_evaluator = relationship(ModelUser, foreign_keys=[second_evaluator_id], lazy='bulk', backref='second_evaluate_card_list')
    content = Column('content', TEXT, nullable=False)
