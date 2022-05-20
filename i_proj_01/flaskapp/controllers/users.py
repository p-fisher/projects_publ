from flaskapp import app
from flask import render_template, redirect, request, session
from flaskapp.models.user import User
from flaskapp.models.idea import Idea
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        # print("**** VALIDATION FAILED ****")
        return redirect('/')
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name'],
        "email": request.form['email'],
        "alias": request.form['alias'],
        # "pwd": request.form['pwd']
        "pwd": bcrypt.generate_password_hash(request.form['pwd'])
    }
    id = User.register(data)
    # session['f_name'] = request.form['f_name']
    session['id'] = id
    # return redirect('/tempsuccess')
    return redirect('/success')



@app.route('/users/detail/<int:id>')
def show_user(id):
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    liked_by_data = {
        "id": id
    }
    user_data = {
        "id": session['id']
    }
    user=User.get_by_id(user_data)
    liked_by=User.get_by_id(liked_by_data)
    # this_idea=Idea.read_idea_with_likes(data)
    # print('***************', this_idea)
    return render_template('user_detail.html',user=user,liked_by=liked_by)




@app.route('/sign_in', methods=['POST'])
def sign_in():
    user = User.sign_in(request.form)
    if not user:
        flash("Invalid Email","sign_in")
        return redirect('/')
    if not bcrypt.check_password_hash(user.pwd, request.form['pwd']):
        flash("Invalid Password","sign_in")
        return redirect('/')
    # session['f_name'] = request.form['f_name']
    session['id'] = user.id
    return redirect('/success')


@app.route('/success')
def made_it():
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    data = {
        "id": session['id']
    }
    user=User.get_by_id(data)
    # ideas=Idea.get_all()
    ideas=Idea.get_ideas_with_users()
    return render_template('success.html',user=user,ideas=ideas)


@app.route('/exit')
def sign_out():
    session.clear()
    return redirect('/')


@app.errorhandler(404)
def not_found(e): # inbuilt function which takes error as parameter
    return f"That's a no-go on the url. Sorry." # defining function