from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import TEXT, VARCHAR
from sqlalchemy.orm import relationship

from model.base import db
from model.model_report_card import ModelReportCard


class ModelSubject(db.Model):
    """SUBJECT model."""

    __tablename__ = 'SUBJECT'

    subject_id = Column('subject_id', VARCHAR(36), primary_key=True)
    report_card_id = Column('report_card_id', VARCHAR(36), ForeignKey('REPORT_CARD.report_card_id'), nullable=False)
    report_card = relationship(ModelReportCard, foreign_keys=[report_card_id], lazy='bulk', backref='subject_list')
    content = Column('content', TEXT, nullable=False)
