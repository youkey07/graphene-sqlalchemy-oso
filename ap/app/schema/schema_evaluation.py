import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_evaluation import ModelEvaluation


class EvaluationAttribute:
    subject_id = graphene.String(description='科目ID')
    evaluated_by_id = graphene.String(description='評価者ID')
    evaluation = graphene.String(description='評価')


class Evaluation(SQLAlchemyObjectType, EvaluationAttribute):
    """REPORT CARD node."""

    class Meta:
        model = ModelEvaluation
        interfaces = (graphene.relay.Node,)
