from app import app, db, bcrypt, login_manager
from flask_login import login_user, current_user, logout_user, login_required
from flask import (request,jsonify,Response)
from flaskapp.models import (User)
from flask_login.mixins import UserMixin

@login_manager.unauthorized_handler
def unauthorized_callback():
    return Response(status=401)

@app.route('/api/login',methods=['GET', 'POST'])
def login():
    content = request.json
    username = content['username']
    password = content['password']
    user = User.query.filter_by(username=username).first()
    if user:
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return Response(status=200, mimetype='application/json')
        else:
            return Response(status=401)
    else:
        return Response(status=401)