from sqlalchemy.orm import Session

from model.base import db
from model.model_user import ModelUser
from model.model_user_role import ModelUserRole
from model.model_role import ModelRole


class CurrentUser:
    def __init__(self, user_id, user_name, school_id, roles):
        self.user_id = user_id
        self.user_name = user_name
        self.school_id = school_id
        self.roles = roles


def get_current_user(user_id):
    try:
        session = Session(bind=db.engine)
        results = session.query(ModelUser, ModelUserRole, ModelRole) \
            .outerjoin(ModelUserRole, ModelUser.user_id == ModelUserRole.user_id) \
            .outerjoin(ModelRole, ModelUserRole.role_id == ModelRole.role_id) \
            .filter(ModelUser.user_id == user_id) \
            .all()

        roles = [r.ModelRole.role_name for r in results if r.ModelRole]

        u = results[0].ModelUser
        return CurrentUser(u.user_id, u.user_name, u.school_id, roles)
    except Exception:
        raise Exception('User not found')
