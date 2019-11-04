from flask import Flask


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    register_blueprints(application)
    application.secret_key='linioexp'
    return application


def register_blueprints(application):
    from app.controllers.login_controller import login_page
    from app.controllers.register_controller import register_page
    application.register_blueprint(login_page)
    application.register_blueprint(register_page)
