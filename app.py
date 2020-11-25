import os
from flask import (
                Flask, flash, render_template,
                redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_symptoms")
def get_symptoms():
    symptoms = list(mongo.db.symptoms.find())
    return render_template("symptoms.html", symptoms=symptoms)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
                        {"username": request.form.get("username").lower()})
        if existing_user:
            flash("This username is already in use!")
            return redirect(url_for("login"))
    # check the passwords
        if request.form.get("password") == request.form.get("confirmpassword"):
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
        else:
            flash("Passwords do not match! Please try again")
            return redirect(url_for("register"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
                        {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(request.form.get("username")))
                return redirect(
                    url_for("get_symptoms", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/add_symptom", methods=["GET", "POST"])
def add_symptom():
    new_symptom = {
            "isolation_status": request.form.get("isolation_status"),
            "symptom_name": request.form.get("symptom_name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "mood": request.form.get("mood")
        }
    mongo.db.symptoms.insert_one(new_symptom)
    flash("Your symptom has been added!")
    status = mongo.db.status.find()
    return render_template("add-symptom.html", status=status)


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_symptoms"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
