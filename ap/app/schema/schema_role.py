import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_role import ModelRole


class RoleAttribute:
    role_id = graphene.ID(description='ロールID')
    role_name = graphene.String(description='ロール名')


class Role(SQLAlchemyObjectType, RoleAttribute):
    """ROLE node."""

    class Meta:
        model = ModelRole
        interfaces = (graphene.relay.Node,)
