import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from model.model_user import ModelUser


class UserAttribute:
    user_id = graphene.ID(description='ユーザID')
    user_name = graphene.String(description='ユーザ名')
    email = graphene.String(description='メールアドレス')
    decrypted_email = graphene.String(description='メールアドレス（復号化）')
    school_id = graphene.String(description='学校ID')
    teacher_id = graphene.String(description='担当教員ID')


class User(SQLAlchemyObjectType, UserAttribute):
    """USER node."""

    class Meta:
        model = ModelUser
        interfaces = (graphene.relay.Node,)
