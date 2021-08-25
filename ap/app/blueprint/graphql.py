from flask import g, request, Blueprint
from flask_graphql import GraphQLView
from werkzeug.exceptions import BadRequest, Unauthorized

from schema.schema import schema
from logger import logging_request, logging_response
from user import get_current_user

graphql_blueprint = Blueprint('graphql', __name__)


# ==============================
# before request
# ==============================
@graphql_blueprint.before_request
def before_request_logger():
    logging_request()


@graphql_blueprint.before_request
def set_current_user():
    user_id = request.headers.get('userId')
    if not user_id:
        raise BadRequest('userId header is not found')

    try:
        g.current_user = get_current_user(user_id)
    except Exception as e:
        raise Unauthorized(e)


# ==============================
# after request
# ==============================
@graphql_blueprint.after_request
def after_request_logger(response):
    logging_response(response)
    return response


# ==============================
# routing
# ==============================
graphql_blueprint.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True))


# ==============================
# error handling
# ==============================
@graphql_blueprint.errorhandler(BadRequest)
def handle_bad_request(e):
    return e, 400


@graphql_blueprint.errorhandler(Unauthorized)
def handle_unauthorized(e):
    return e, 401
