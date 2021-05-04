from flask import Flask, redirect, url_for, render_template, request
import pymysql


db = pymysql.connect("localhost" , "root" , "" , "stores") # This connects to the stores Database...
app = Flask(__name__)

# Basic functions for the navbar.

@app.route("/") # 127.0.0.1:5000/
def home():
	return render_template("Home.html") # Calls the HTML file from the template folder.

@app.route("/home") # 127.0.0.1:5000/home
def home2():
    return render_template("Home.html")

@app.route("/store") # 127.0.0.1:5000/store (Hidden from the user)
def store():
	return render_template("Store.html")



@app.route("/login" , methods=["POST" , "GET"]) # 127.0.0.1:5000/login
def login():

	error = None # Stores error for login page.

	if request.method == "POST": # If the Method is POST
		
		if request.form["Username"] != "admin" or request.form["Password"] != "admin": # This allows for login.

			error = "Invalid Username or Password." # Returns the error to the user on the HTML page.

		else:

			return redirect(url_for("admin")) # If singned in correctly, it would send to the special admin page.

	return render_template("Login.html" , error=error) # Returns to Login page, along with an error, if credentials are wrong.


# These are the admin options, only when signed on.

@app.route("/login/admin/genres/suggestions" , methods=["POST" , "GET"]) # 127.0.0.1:5000/login/admin/genres/suggestions
def admin():

	cursor = db.cursor()
	sql = "SELECT * FROM genre" # SQL Query.
	cursor.execute(sql) # Executes the Query.
	results = cursor.fetchall() # Stores results in variable.

	# This section was supposed to allow the admin to delete suggestions.
	# It did not work as we planned, but it shows which checkbox is selected on the console.
	i = 0
	if request.method == "POST":
		for num , val in results:

			#cursor = db.cursor()
			#sql = "DELETE FROM genre WHERE genre.GenreID = ?" , (i)
			#cursor.execute(sql)

			#print(num)
			i = i + 1
			print(request.form.getlist(str(i))) 
			
	


	return render_template("Admin.html" , results=results) # Returns results to Admin.html


@app.route("/login/admin/storetypes/suggestions" , methods=["POST" , "GET"]) # 127.0.0.1:5000/login/admin/storetypes/suggestions
def admin2():

	cursor = db.cursor()
	sql = "SELECT * FROM new_store_submition"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("Admin2.html" , results=results)


@app.route("/submit" , methods=["POST" , "GET"]) # 127.0.0.1:5000/submit
def submit():
	# This allows for 1 submission, the store genre.

	if request.method == "POST":
		  
		StoreType = request.form["StoreType"] # Gets the information from the textbox specifically "name" attribute.
		cursor = db.cursor()
		sql = "INSERT INTO genre(StoreType) VALUES(%s)" # Looks for a String
		cursor.execute(sql, (StoreType)) # Executes the Query
		db.commit() # Confirms with the database.

	return render_template("Submit.html")


@app.route("/genre-submission" , methods=["POST" , "GET"]) # 127.0.0.1:5000/genre-submission
def genreSubmition():

	# This is for the second submission accordion

	if request.method == "POST": # The following gets information from the "name" attribute.  Does the same as above...

		StoreType = request.form["StoreType"]
		StoreName = request.form["StoreName"]
		StreetAddress = request.form["StreetAddress"]
		StoreCity = request.form["StoreCity"]
		ZipCode = request.form["ZipCode"]
		PhoneNumber = request.form["PhoneNumber"]
		County = request.form["County"]
		Website = request.form["Website"]

		cursor = db.cursor()
		sql = "INSERT INTO new_store_submition(StoreType , StoreName , StreetAddress , StoreCity , ZipCode , PhoneNumber , County , Website) VALUES (%s , %s, %s, %s, %s, %s , %s, %s)"
		cursor.execute(sql, (StoreType , StoreName , StreetAddress , StoreCity , ZipCode , PhoneNumber , County , Website))
		db.commit()

	return render_template("Submit.html") 


#These 4 functions shows the database in an organized table.
@app.route("/videogames") # 127.0.0.1:5000/videogames
def videoGames():
	cursor = db.cursor() # Interacts with the database.
	sql = "SELECT * FROM VideoGames" # Takes everything from the table.
	cursor.execute(sql) # Executes.
	results = cursor.fetchall() # Gathers all the rows from database, is stored as a List.
	return render_template("videoGames.html" , results=results) # Returns to the html page with the table, results.


@app.route("/crystals") # 127.0.0.1:5000/crystals
def crystals():
	cursor = db.cursor()
	sql = "SELECT * FROM Crystals"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("Crystals.html" , results=results)


@app.route("/records") # 127.0.0.1:5000/records
def records():
	cursor = db.cursor()
	sql = "SELECT * FROM Records"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("Records.html" , results=results)


@app.route("/comic-books") # 127.0.0.1:5000/comic-books
def comics():
	cursor = db.cursor()
	sql = "SELECT * FROM Comics"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("Comic-Books.html" , results=results)


@app.route("/books") # 127.0.0.1:5000/books
def books():
	cursor = db.cursor()
	sql = "SELECT * FROM Books"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("Books.html" , results=results)

@app.route("/antiques") # 127.0.0.1:5000/antiques
def antiques():
	cursor = db.cursor()
	sql = "SELECT * FROM Antiques"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template("Antiques.html" , results=results)


if __name__ == "__main__":
	
	app.run(debug=True) # Debug is very useful here; saved me a ton.

	