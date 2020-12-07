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

# view for the main page


@app.route("/")
@app.route("/get_symptoms")
def get_symptoms():
    symptoms = list(mongo.db.symptoms.find())
    return render_template("symptoms.html", symptoms=symptoms)

# view for the search bar beneath the list of symptoms on the home page


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        symptoms = list(mongo.db.symptoms.find({"$text": {"$search": query}}))
        return render_template("symptoms.html", symptoms=symptoms)

# views for the registratio and login pages


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
            return redirect(url_for("my_symptoms", username=session["user"]))
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
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}".format(request.form.get("username")))
                return redirect(
                    url_for("my_symptoms", username=session["user"]))
            else:
                # invalid password match
                return render_template("error_page.html")
        else:
            # username doesn't exist
            return render_template("error_page.html")
    return render_template("login.html")

# view for the users profile page


@app.route("/my_symptoms/<username>", methods=["GET", "POST"])
def my_symptoms(username):
    # applicable to GET and POST methods
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    status = mongo.db.status.find()
    symptoms = list(mongo.db.symptoms.find({"symptom_recipient": username}))
    # the user adds a symptom from the add symptom form,
    # which is on the my symptoms html template
    if request.method == "POST":
        new_symptom = {
            "isolation_status": request.form.get("isolation_status"),
            "symptom_name": request.form.get("symptom_name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "mood": request.form.get("mood"),
            "symptom_recipient": session["user"]
        }
        mongo.db.symptoms.insert_one(new_symptom)
        return redirect(url_for(
            "my_symptoms", username=session['user']))
    # this html template also, lists the current symtpoms of the user
    return render_template(
        "my_symptoms.html",
        username=username, symptoms=symptoms, status=status)

# view for the add symtpom functionality


@app.route("/add_symptom", methods=["GET", "POST"])
def add_symptom():
    if request.method == "POST":
        status = mongo.db.status.find()
        new_symptom = {
                "isolation_status": request.form.get("isolation_status"),
                "symptom_name": request.form.get("symptom_name"),
                "description": request.form.get("description"),
                "start_date": request.form.get("start_date"),
                "mood": request.form.get("mood"),
                "symptom_recipient": session["user"]
            }
        mongo.db.symptoms.insert_one(new_symptom)
        flash("Your symptom has been added!")
        return redirect(url_for(
            "my_symptoms", username=session['user']))
    else:
        return render_template("my_symptoms.html", status=status)

# view for the edit symtpom functionality


@app.route("/edit_symptom/<symptom_id>", methods=["GET", "POST"])
def edit_symptom(symptom_id):
    if request.method == "POST":
        updated_symptom = {
            "isolation_status": request.form.get("isolation_status"),
            "symptom_name": request.form.get("symptom_name"),
            "description": request.form.get("description"),
            "start_date": request.form.get("start_date"),
            "mood": request.form.get("mood"),
            "symptom_recipient": session["user"]
            }
        mongo.db.symptoms.update_one(
            {"_id": ObjectId(symptom_id)},
            {"$set": updated_symptom})
        flash("Your symptom has been updated!")
        return redirect(url_for("my_symptoms", username=session['user']))
    symptom = mongo.db.symptoms.find_one({"_id": ObjectId(symptom_id)})
    status = mongo.db.status.find()
    return render_template("edit_symptom.html", status=status, symptom=symptom)

# view for the delete symtpom functionality


@app.route("/delete_symptom/<symptom_id>")
def delete_symptom(symptom_id):
    mongo.db.symptoms.remove(
            {"_id": ObjectId(symptom_id)})
    flash("Your symptom has been deleted! Why not add another?")
    return redirect(url_for("my_symptoms", username=session['user']))

# view for the log out functionality


@app.route("/logout")
def logout():
    flash("You have been logged out. See you soon and take care!")
    session.pop("user")
    return redirect(url_for("get_symptoms"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
