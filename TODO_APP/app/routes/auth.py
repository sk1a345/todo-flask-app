from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

# This means you are making a blueprint called auth that handles login/logout. It’s just a section of your app focused on authentication 
USER_CREDENTIALS = {
    "username": "admin",
    "password": "1234"
}

@auth_bp.route("/login",methods=['GET',"POST"])
def login():
    if request.method == "POST":
        username=request.form.get("username")
        password = request.form.get("password")

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash("Login Successful", "success")
            return redirect(url_for("tasks.view_tasks"))
        else:
            flash("Invalid username or password","danger")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user",None)
    flash("Logged Out","info")
    return redirect(url_for('auth.login'))

