import os
from flask import(
    Flask, flash, render_template,
    redirect, request, session, url_for)
if os.path.exists("env.py"):
    import env
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_symptoms")
def get_symptoms():
    symptoms = mongo.db.symptoms.find()
    return render_template("symptoms.html", symptoms=symptoms)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
                        {"username": request.form.get("username").lower()})
        if existing_user:
            flash("This username is already in use!")
            return redirect(url_for("register"))
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
