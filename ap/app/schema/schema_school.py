import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_school import ModelSchool


class SchoolAttribute:
    school_id = graphene.ID(description='学校ID')
    school_name = graphene.String(description='学校名')


class School(SQLAlchemyObjectType, SchoolAttribute):
    """SCHOOL node."""

    class Meta:
        model = ModelSchool
        interfaces = (graphene.relay.Node,)
