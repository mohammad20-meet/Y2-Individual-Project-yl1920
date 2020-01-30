from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/home')
def home(): 
	return render_template("home.html")

@app.route('/Describtion')
def Describtion():
	return render_template("Describtion.html")

@app.route('/games')
def games():
	return render_template("games.html")

@app.route('/games/Dino')
def Dino():
	return render_template("Dino.html")
@app.route('/games/TicTacToe')
def tic():
	return render_template("tic.html")

@app.route('/games/Annoy')
def Annoy():
	return render_template("Cancer.html")

@app.route('/scoreboards')
def scoreboards():
	return render_template("scoreboards.html")

@app.route('/Login', methods=['GET', 'POST'])
def Login():
	if request.method == 'GET':
		return render_template("Login.html")
	else:
		Name = request.form['name']
		ps = request.form['psw']
		print(db_login(Name, ps))
		if db_login(Name, ps) == True:
			login_session['logged_in']="TRUE"
			return render_template("home.html",Name = Name)
		else:
			return render_template("Login.html", msg="wrong username or password") 


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		G = request.form['Gmail']
		N = request.form['name']
		ps = request.form['psw']
		Signup(G ,N ,ps)
		return render_template("Login.html",Name = N)


if __name__ == '__main__':
	app.run(debug=True)