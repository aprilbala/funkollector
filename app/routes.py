from app import app
from flask import Flask, render_template, flash
from flask import request, redirect
from forms import AddFunkoForm, AddToWishlistForm
import webbrowser

pops = []
wishes = []

# do something with app...
@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/")
def main():
    return render_template('welcomepage.html')

@app.route("/welcomepage")
def welcomepage():
    return render_template('welcomepage.html')

@app.route("/mycollection")
def mycollection():
	return render_template('mycollection.html', pops=pops)

@app.route("/mywishlist")
def mywishlist():
    return render_template('mywishlist.html', wishes=wishes)

@app.route('/addafunko', methods=['GET', 'POST'])
def addafunko():
	# form = AddFunkoForm()
	form = AddFunkoForm()
	
	if request.method == 'POST' and form.validate():
		pops.append(request.form)

	return render_template('addafunko.html', form=form)
	redirect('/mycollection')

@app.route('/addtowishlist', methods=['GET', 'POST'])
def addtowishlist():
	form = AddToWishlistForm()
	
	if request.method == 'POST' and form.validate():
		wishes.append(request.form)

	return render_template('addtowishlist.html', form=form)