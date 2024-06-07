# create page function
from flask import Flask,flash

def create_page():
    app = Flask(__name__)
    
    app.app_context().push()
    app.secret_key = "1212"
    from .views import views

    app.register_blueprint(views,url_prefix='/')


    return app