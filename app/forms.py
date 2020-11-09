from flask_wtf import Form
from wtforms import Form, TextField, IntegerField, SelectField, SubmitField

# form for adding funko pop to collection
class AddFunkoForm(Form):
	funkoname = TextField("Funko Name")
	funkonum = IntegerField("#")
	funkoseries = TextField("Funko Series")
 	# price = DecimalField("Price ($)")
	store = TextField("Store / Place of Purchase")
 	submit = SubmitField("Add")

# form for adding funko pop to wishlist
class AddToWishlistForm(Form):
	funkoname = TextField("Funko Name")
	funkonum = IntegerField("#")
	funkoseries = TextField("Funko Series")
 	price = IntegerField("Price ($)")
	store = TextField("Store / Place of Purchase")
 	submit = SubmitField("Add")