from flask import Flask, render_template

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app

    # attach routes and custom error pages here

    return app
