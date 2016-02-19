from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	__tablename__="user"

	#fields
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(180))
	fullname = db.Column(db.String(180))
	email = db.Column(db.String(180))
	address = db.Column(db.String(180))
	phonenumber = db.Column(db.Integer)
	password = db.Column(db.String(180))
	def __init__(self,username,fullname,email,address,phonenumber,password):
		self.username = username
		self.fullname = fullname
		self.email = email
		self.address = address
		self.phonenumber = phonenumber
		self.password = password
	def __repr__(self):
		return "<User {}>".format(self.username)

class Hotels(db.Model):
	__tablename__="hotels"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(180))
	address = db.Column(db.String(180))
	zipcode = db.Column(db.Integer)
	city = db.Column(db.String(180))
	province = db.Column(db.String(180))
	country = db.Column(db.String(180))
	price = db.Column(db.String(180))
	def __init__(self,name,address,zipcode,city,province,country,price):
		self.name = name
		self.address = address
		self.zipcode = zipcode
		self.city = city
		self.province = province
		self.country = country
		self.price = price
	def __repr__(self):
		return "<Hotels {}>".format(self.name)

class City(db.Model):
	__tablename__ = "city"
	id = db.Column(db.Integer,primary_key=True)
	city = db.Column(db.String(180))
	code = db.Column(db.String(180))
	def __init__(self,city,code):
		self.city = city
		self.code = code
	def __repr__(self):
		return "<City {}".format(self.city)

class Province(db.Model):
	__tablename__="province"
	id = db.Column(db.Integer,primary_key=True)
	province = db.Column(db.String(180))
	code = db.Column(db.String(180))
	def __init__(self,province,code):
		self.province = province
		self.code = code
	def __repr__(self):
		return "<Province {}>".format(self.province)

class Country(db.Model):
	__tablename__ = "country"
	id = db.Column(db.Integer,primary_key=True)
	country = db.Column(db.String(180))
	code = db.Column(db.String(180))
	def __init__(self,country,code):
		self.country = country
		self.code = code
	def __repr__(self):
		return "<Country {}>".format(self.country)

class Hotel_facility(db.Model):
	__tablename__ = "hotel_facility"
	id = db.Column(db.Integer,primary_key=True)
	hotelid = db.Column(db.Integer,db.ForeignKey("hotels.id"))
	hotel = db.relationship("Hotels",
			backref=db.backref('hotel_facility',lazy="dynamic"))
	garage = db.Column(db.Integer)
	carports = db.Column(db.Integer)
	swimmingpoll = db.Column(db.Integer)
	def __init__(self,hotelid,garage,carports,swimmingpoll):
		self.hotelid = hotelid
		self.garage = garage
		self.carports = carports
		self.swimmingpoll = swimmingpoll
	def __repr__(self):
		return "<Hotel_facility {}>".format(self.hotelid)

class Reservation(db.Model):
	__tablename__="reservation"
	id = db.Column(db.Integer,primary_key=True)
	userid = db.Column(db.Integer,db.ForeignKey("user.id"))
	user = db.relationship("User",
			backref=db.backref("reservation",lazy="dynamic"))
	hotelid = db.Column(db.Integer,db.ForeignKey("hotels.id"))
	hotel = db.relationship("Hotels",
			backref=db.backref("reservation",lazy="dynamic"))
	reservationcode=db.Column(db.Integer)
	checkindate = db.Column(db.DateTime)
	checkoutdate = db.Column(db.DateTime)
	roomnumber = db.Column(db.Integer)
	room = db.Column(db.Integer)
	adult = db.Column(db.Integer)
	amount = db.Column(db.String(180))
	night = db.Column(db.Integer)
	status = db.Column(db.Integer)
	checkin_status = db.Column(db.Integer)
	checkout_status = db.Column(db.Integer)
	def __init__(self,userid,hotelid,reservationcode,checkindate,checkoutdate,roomnumber,room,adult,amount,night,status,checkin_status,checkout_status):
		self.userid = userid
		self.hotelid = hotelid
		self.reservationcode = reservationcode
		self.checkindate = checkindate
		self.checkoutdate= checkoutdate
		self.roomnumber = roomnumber
		self.room = room
		self.adult = adult
		self.amount = amount
		self.night = night
		self.status = status
		self.checkin_status = checkin_status
		self.checkout_status = checkout_status
	def __repr__(self):
		return "<Reservation {}>".format(self.userid)

class Roles(db.Model):
	__tablename__ = "roles"
	id = db.Column(db.Integer,primary_key=True)
	role = db.Column(db.String(180))
	description = db.Column(db.String(180))
	def __init__(self,role,description):
		self.role = role
		self.description = description
	def __repr__(self):
		return "<Roles {}>".format(self.role)

class User_roles(db.Model):
	__tablename__="user_roles"
	id = db.Column(db.Integer,primary_key=True)
	roleid = db.Column(db.Integer,db.ForeignKey("roles.id"))
	role = db.relationship("Roles",
			backref=db.backref("roles",lazy="dynamic"))
	userid = db.Column(db.Integer,db.ForeignKey("user.id"))
	user =db.relationship("User",
			backref=db.backref("users",lazy="dynamic"))
	def __init__(self,roleid,userid):
		self.roleid=roleid
		self.userid=userid
	def __repr__(self):
		return "<User_roles {}>".format(self.roleid)

class Profile(db.Model):
	__tablename__ = "profile"
	id = db.Column(db.Integer,primary_key=True)
	userid = db.Column(db.Integer,db.ForeignKey("user.id"))
	user = db.relationship("User",
			backref=db.backref('profile',lazy="dynamic"))
	birthdate= db.Column(db.Integer)
	birthplace=db.Column(db.String(180))
	gender = db.Column(db.String(180))
	def __init__(self,userid,birthdate,birthplace,gender):
		self.userid = userid
		self.birthdate = birthdate
		self.birthplace = birthplace
		self.gender = gender
	def __repr__(self):
		return"<Profile {}>".format(self.userid)