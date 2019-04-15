from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'ilikecoolstuffthatisfuntodo'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)

def getLanguages():
   mysql = connectToMySQL("flask_survey")
   return mysql.query_db("SELECT * FROM languages;")

def getLocations():
   mysql = connectToMySQL("flask_survey")
   query = "SELECT * FROM locations;"
   return mysql.query_db(query)

def getLanguage(id):
   mysql = connectToMySQL("flask_survey")
   query = "SELECT * FROM languages WHERE id=%(id)s;"
   data = {
      "id": id
   }
   return mysql.query_db(query, data)[0]

def getLocation(id):
   mysql = connectToMySQL("flask_survey")
   query = "SELECT * FROM locations WHERE id=%(id)s;"
   data = {
      "id": id
   }
   return mysql.query_db(query, data)[0]

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/success')
def success():
   return render_template("success.html")

@app.route('/register_user', methods=['POST'])
def result():
   print('user submitted form')
   print(request.form)
   query = """INSERT INTO users (first_name, last_name, email_address, password) 
               VALUES (%(fname)s, %(lname)s,%(email)s, %(password)s);"""
   if(len(request.form["firstName"]) < 1):
      flash("Please enter a first name", 'firstname')
   if(len(request.form["lastName"]) < 1):
      flash("Please enter a last name", 'lastname')
   if(len(request.form["emailAddress"]) < 1 or not EMAIL_REGEX.match(request.form["emailAddress"])):
      flash("Please enter a valid email address", 'email')
   if(request.form["passwordMain"] != request.form["passwordRepeat"]):
      flash("Passwords do not match", "passwordRepeat")
   if(len(request.form["passwordMain"]) < 1):
      flash("Please enter a password", "passwordMain")
   if(len(request.form["passwordRepeat"]) < 1):
      flash("Please enter a password", "passwordRepeat")
   
   if not '_flashes' in session.keys():
      values = {
         'fname': request.form["firstName"],
         'lname': request.form["lastName"],
         'email': request.form["emailAddress"],
         'password': bcrypt.generate_password_hash(request.form["passwordMain"])
      }
      mysql = connectToMySQL("flask_login_reg")
      user = mysql.query_db(query, values)
      flash("email successfully added to database!")
      session["myUserId"] = user
      session["isLoggedIn"] = True
      return redirect('/success')
   else:
      session.clear()
      return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)