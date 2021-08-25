import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_user_role import ModelUserRole


class UserRoleAttribute:
    user_id = graphene.ID(description='ユーザID')
    role_id = graphene.ID(description='ロールID')


class UserRole(SQLAlchemyObjectType, UserRoleAttribute):
    """USER_ROLE node."""

    class Meta:
        model = ModelUserRole
        interfaces = (graphene.relay.Node,)
