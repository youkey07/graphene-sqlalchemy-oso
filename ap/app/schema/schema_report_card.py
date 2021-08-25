import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_report_card import ModelReportCard


class ReportCardAttribute:
    report_card_id = graphene.ID(description='成績表ID')
    user_id = graphene.String(description='所有者ID')
    first_evaluator_id = graphene.String(description='一次評価者ID')
    second_evaluator_id = graphene.String(description='二次評価者ID')
    content = graphene.String(description='内容')


class ReportCard(SQLAlchemyObjectType, ReportCardAttribute):
    """REPORT CARD node."""

    class Meta:
        model = ModelReportCard
        interfaces = (graphene.relay.Node,)
