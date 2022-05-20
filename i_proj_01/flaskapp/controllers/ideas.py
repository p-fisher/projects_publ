from flaskapp import app
from flask import render_template, redirect, request, session, url_for
from flaskapp.models.user import User
from flaskapp.models.idea import Idea
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/create/idea',methods=['POST'])
def create_idea():
    # if 'user_id' not in session:            # session stuff a mess save for later
    #     return redirect('/logout')
    if not Idea.validate_idea(request.form):
        return redirect('/success')
    data = {
        "user_id": request.form["user_id"],
        "summary": request.form["summary"],
    }
    Idea.add_idea(data)
    return redirect('/success')


@app.route('/delete/idea/<int:id>')
def delete_idea(id):
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    data = {
        "id":id
    }
    Idea.delete(data)
    return redirect('/success')




@app.route("/like/idea/<int:id>")
def like_idea(id):
    # Go to db, add idea id and user id to like table.
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    data = {
        "idea_id": id,
        "user_id": session['id']
    }
    Idea.like_idea(data)
    return redirect('/success')




@app.route('/details/<int:id>')
def show_idea(id):
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    data = {
        "id": id
    }
    user_data = {
        "id": session['id']
    }
    user=User.get_by_id(user_data)
    this_idea=Idea.read_idea_with_likes(data)
    # print('***************', this_idea)
    return render_template('details.html',user=user,idea=this_idea)

# def show_idea(id):
#     if 'id' not in session:
#         return redirect('/exit')           # used only in GET method routes
#     data = {
#         "id": id
#     }
#     user_data = {
#         "id": session['id']
#     }
#     user=User.get_by_id(user_data)
#     this_idea=Idea.get_by_id(data)
#     # ideas=Idea.get_ideas_with_users()
#     return render_template('details.html',user=user,idea=this_idea) # ,ideas=ideas

# @app.route('/add')
# def new_idea():
#     if 'id' not in session:
#         return redirect('/exit')           # used only in GET method routes
#     user_data = {
#         "id":session['id']
#     }
#     user=User.get_by_id(user_data)
#     return render_template('add_idea.html', user=user)


@app.route('/edit_load_idea/<int:id>')
def edit_load_idea(id):
    if 'id' not in session:
        return redirect('/exit')           # used only in GET method routes
    data = {
        "id": id
    }
    user_data = {
        "id":session['id']
    }
    user=User.get_by_id(user_data)
    this_idea=Idea.get_by_id(data)
    return render_template("edit_idea.html",user=user,idea=this_idea)



@app.route('/edit_save_idea', methods=['POST'])
def edit_save_idea():
    data = {
        "id": request.form['id'],
        "summary": request.form["summary"],
        # "user_id": session["id"]
    }
    Idea.update(data)
    return redirect('/success')



# having these enabled in both controllers breaks the app

# @app.route('/exit', methods=['POST'])
# def sign_out():
#     session.clear()
#     return redirect('/')


# @app.errorhandler(404)
# def not_found(e): # inbuilt function which takes error as parameter
#     return f"That's a no-go on the url. Sorry." # defining function"""