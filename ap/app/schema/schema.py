import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

import model
import schema


class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()

    # School
    school_list = SQLAlchemyConnectionField(schema.School)

    school = graphene.Field(lambda: schema.School,
                            school_id=graphene.ID())

    def resolve_school(self, info, school_id):
        query = schema.School.get_query(info)
        result = query.filter(model.ModelSchool.school_id == school_id).first()
        return result

    # User
    user_list = SQLAlchemyConnectionField(schema.User)

    user = graphene.Field(lambda: schema.User,
                          user_id=graphene.ID())

    def resolve_user(self, info, user_id):
        query = schema.User.get_query(info)
        result = query.filter(model.ModelUser.user_id == user_id).first()
        return result


schema = graphene.Schema(query=Query)
