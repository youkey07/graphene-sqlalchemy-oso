from sqlalchemy import Column, ForeignKey, cast, func
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship, column_property

from config.config import PASSPHRASE
from model.base import db
from model.model_school import ModelSchool


class ModelUser(db.Model):
    """USER model."""

    __tablename__ = 'USER'

    user_id = Column('user_id', VARCHAR(36), primary_key=True)
    user_name = Column('user_name', VARCHAR(36), nullable=False)
    email = Column('email', VARCHAR(128), nullable=False)
    decrypted_email = column_property(
        cast(
            func.aes_decrypt(
                func.unhex(email), func.unhex(func.sha2(PASSPHRASE, 512))
            ),
            VARCHAR(charset='utf8mb4'),
        )
    )
    school_id = Column('school_id', VARCHAR(36), ForeignKey('SCHOOL.school_id'), nullable=False)
    school = relationship(ModelSchool, foreign_keys=[school_id], lazy='bulk', backref='user_list')
    teacher_id = Column('teacher_id', VARCHAR(36), ForeignKey('USER.user_id'), nullable=False)
    teacher = relationship('ModelUser', remote_side=[user_id], lazy='bulk', backref='student_list')
