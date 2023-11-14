from website import create_app

# when you put __init__.py file in a folder it becomes a python package, we can import anything from __init__.py file

app = create_app()

if __name__ == '__main__': #only if we run this file server is going to run otherwise not
  app.run(debug=True) # web server is going to run , debug = true means if we make any changes in out code the server will automatically rerun
  