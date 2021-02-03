from flask_wtf import Form
from wtforms import (TextField, SelectMultipleField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField)

from wtforms import validators, ValidationError

class ContactForm(Form):
   dpName = SelectField('dpName', choices= ['NMMT','CMRL','HMRL(L&T Metro)','Narayana Hospital', 'NMMT Ghansoli Depot', 'Silver Sands Serenity', 'SRS Shanti Nagar Depot Bangalore','NMMT Turbhe'])
   alertName = TextField("Name Of Alert")
   threshold = IntegerField("Threshold")
   number = IntegerField("Input review period")
   reviewP = SelectField('reviewP', choices = ['Days','Weeks','Months','Year'])
   stm = SelectField('Statitical Methods', choices = ['min','max','avg','sum','len','last'])
   oPerator = SelectField('Operator', choices=['<','>','='])
   
   EdgeId = SelectField('EdgeId', choices = ['c00187', 'e76f8b', '42d972', '7039b3', 'bfe529', '71b607','6d4942', '98a03c', '9cd1c9','07c436', 'f1a6fc', '76efcf'])
   submit = SubmitField("Send")