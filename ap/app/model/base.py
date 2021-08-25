import os

from flask import g, current_app
from sqlalchemy_oso.flask import AuthorizedSQLAlchemy
from sqlalchemy_bulk_lazy_loader import BulkLazyLoader

from config.config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

db_url = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME
)

BulkLazyLoader.register_loader()
db = AuthorizedSQLAlchemy(
    get_oso=lambda: current_app.oso,
    get_user=lambda: getattr(g, "current_user", None),
    get_action=lambda: "read"
)
