from pathlib import Path

from flask import Flask
from oso import Oso
from sqlalchemy_oso import register_models

from model.base import db, db_url
from blueprint.graphql import graphql_blueprint


def create_app():
    app = Flask(__name__)

    # sqlalchemy
    db.init_app(app)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=db_url,
    )

    # oso
    oso = Oso()
    register_models(oso, db.Model)
    oso.load_file(Path(__file__).parent / "policy.polar")
    app.oso = oso
    
    app.register_blueprint(graphql_blueprint)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
