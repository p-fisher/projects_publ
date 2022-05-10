from flaskapp import app

#every new controller file needs to be imported here
from flaskapp.controllers import users
from flaskapp.controllers import ideas

app.secret_key="Get into your handbasket and head south."

if __name__=="__main__":   # Ensure this runs directly and not from a diff module
    app.run(debug=True)    # Run the app in debug mode.