#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request

app = Flask(__name__)
app.secret_key = "any random string"

## If the user hits the root of our API
@app.route("/")
def index():
  ## if the key "username" has a value in session
  if "username" in session:
    username = session["username"]
    age = session.get("age", "Unknown")
    return f"Logged in as {username}, Age: {age} <br>" + \
      "<b><a href='/logout'>click here to log out</a></b>"

  ## if the key "username" does not have a value in session
  return "You are not logged in <br><a href='/login'>click here to log in</a>"

## If the user hits /login with a GET or POST
@app.route("/login", methods=["GET", "POST"])
def login():
    ## if you sent us a POST because you clicked the login button
    if request.method == "POST":
        ## request.form["xyzkey"]: use indexing if you know the key exists
        ## request.form.get("xyzkey"): use get if the key might not exist
        session["username"] = request.form.get("username")
        session["age"] = request.form.get("age")
        return redirect(url_for("index"))

    ## return this HTML data if you send us a GET
    return """
    <form action="" method="post">
        <p>Username: <input type="text" name="username"></p>
        <p>Age: <input type="number" name="age"></p>
        <p><input type="submit" value="Login"></p>
    </form>
    """

@app.route("/logout")
def logout():
    # remove the username and age from the session if they are there
    session.pop("username", None)
    session.pop("age", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

