from flask import Flask

def create_app():
  app = Flask(__name__) #intialize flask (name of the file) 
  app.config['SECRET_KEY'] = "hjgdhgshh jsjdjkds" # intialize a secret key for app
  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  
  return app