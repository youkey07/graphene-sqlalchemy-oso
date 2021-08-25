import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_subject import ModelSubject


class SubjectAttribute:
    subject_id = graphene.ID(description='科目ID')
    report_card_id = graphene.String(description='成績表ID')
    content = graphene.String(description='内容')


class Subject(SQLAlchemyObjectType, SubjectAttribute):
    """REPORT CARD node."""

    class Meta:
        model = ModelSubject
        interfaces = (graphene.relay.Node,)
