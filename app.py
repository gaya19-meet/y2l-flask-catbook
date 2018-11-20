from flask import Flask
from flask import render_template, redirect, request
from database import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>')
def cat_html(id):
	
	cat = session.query(Cat).filter_by(id=id).first()
	return render_template("cat.html", cat=cat)

@app.route('/addcat', methods=['GET','POST'])
def add_cat():
	if request.method == "GET":
		 return render_template("add_cat.html")
	else:
		catname1 = request.form["cat_name"]
		create_cat(catname1) 
		return redirect('/')




if __name__ == '__main__':
   app.run(debug = True)




