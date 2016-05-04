
#error: no module named flask_wtf
from flask_wtf import Form
from wtforms import SubmitField, PasswordField, StringField, validators
from models import User

class SigninForm(Form):
  email = StringField("Email",  [validators.InputRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.input_required("Please enter a password.")])
  submit = SubmitField("Sign In")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

  def validate(self):
    if not Form.validate(self):
      return False

    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False

class SignupForm(Form):
  firstname = StringField("First name",  [validators.InputRequired()])
  lastname = StringField("Last name",  [validators.InputRequired()])
  email = StringField("Email",  [validators.InputRequired(), validators.Email()])
  password = PasswordField('Password', [validators.InputRequired()])
  submit = SubmitField("Create account")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

  def validate(self):
    if not Form.validate(self):
      return False

    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True