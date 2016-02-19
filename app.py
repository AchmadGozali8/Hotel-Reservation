from flask import Flask,render_template,request,redirect,session
from models import db,User,Hotels,City,Province,Country,Hotel_facility,Reservation,Roles,User_roles,Profile
app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)

#hotel
@app.route("/hotel",methods=["POST","GET"])
def hotel():
	if request.method=="GET":
		hotel = Hotels.query.all()
		return render_template("index.html",**locals())

@app.route("/hotel/<int:id>",methods=["POST","GET"])	
def hotel_detail(id):
	if request.method == "GET":
		hotel = Hotels.query.get(id)
		return render_template("hotel_detail.html",**locals())

@app.route("/hotel/new",methods=["POST","GET"])
def new_hotel():
	if request.method=="POST":
		name = request.form.get("name",None)
		address = request.form.get("address",None)
		zipcode = request.form.get("zipcode",None)
		city = request.form.get("city",None)
		province = request.form.get("province",None)
		country = request.form.get("country",None)
		price = request.form.get("price",None)

		new = Hotels(name,address,zipcode,city,province,country,price)
		db.session.add(new)
		db.session.commit()
		return redirect("/hotel")
	return render_template("add_hotel.html",**locals())

@app.route("/hotel/update/<int:id>",methods=["POST","GET"])
def update(id):
	if request.method=="POST":
		new_price = request.form.get("price",None)
		harga = Hotels.query.get(id)
		harga.price = new_price
		db.session.add(harga)
		db.session.commit()
		return redirect("/hotel")
	harga = Hotels.query.get(id)
	return render_template("update_price.html",**locals())

@app.route("/hotel/delete/<int:id>",methods=["POST","GET"])
def delete_hotel(id):
	hotel = Hotels.query.get(id)
	db.session.delete(hotel)
	db.session.commit()
	return redirect("/hotel")

@app.route("/hotel/deleteall",methods=["POST","GET"])
def delete_all():
	hotel = Hotels.query.all()
	db.session.delete(hotel)
	db.session.commit()
	return redirect('/hotel')

#user
#registrasi

@app.route("/registrasion",methods=["POST","GET"])
def register():
	if request.method=="POST":
		username = request.form.get("username",None)
		fullname = request.form.get("fullname",None)
		email = request.form.get("email",None)
		address = request.form.get("address",None)
		phonenumber = request.form.get("phonenumber",None)
		password = request.form.get("password",None)
		role = request.form.get("role",None)
		if username=="":
			error="please input your username"
		elif fullname == "":
			error = "please input your fullname"
		elif email == "":
			error = "please input your email"
		elif address == "":
			error = "please input your address"
		elif phonenumber == "":
			error = "please input your phone number"
		elif password == "":
			error = "please input your password"
		user = User(username,fullname,email,address,phonenumber,password)
		db.session.add(user)
		db.session.commit()
		#save user information
		session["userid"] = user.id
		userid = session.get("userid",None)

		#role id
		pilihan = Roles.query.get(id)

		session["roleid"]=pilihan.id
		roleid = session.get("roleid",None)
		if role == "admin":
			user_role=User_roles(userid,roleid)
			db.session.add(user_role)
			db.session.commit()
		elif role == "memeber":
			db.session.add(userid,roleid==2)
			db.session.commit()
		#if role == 1:
		#	admin = session.query(Role).filter(Role.role=="admin")
		#	db.session.add(userid,admin)
		#	db.sesssion.commit()
		#elif role == 2:
		#	member = session.query(Role).filter(Role.role=="member")
		#	db.session.add(userid,member)
		#	db.sesssion.commit()
		return redirect("/hotel")
	return render_template("registrasi.html",**locals())
if __name__=="__main__":
	app.run()