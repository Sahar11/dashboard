from flask import Flask

def create_app():
  app = Flask(__name__) #intialize flask (name of the file) 
  app.config['SECRET_KEY'] = "hjgdhgshh jsjdjkds" # intialize a secret key for app

  return app