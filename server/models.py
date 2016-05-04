from app import db
from werkzeug import generate_password_hash, check_password_hash

class CrowdfundingProject(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Building_id = db.Column(db.Integer, nullable = True, default = None)
    Address = db.Column(db.String(256), nullable = True, default = None)
    City = db.Column(db.String(48), nullable = True, default = None)
    State = db.Column(db.String(48), nullable = True, default = None)
    GPS_Lat = db.Column(db.Integer, default = 0)
    GPS_Lon = db.Column(db.Integer, default = 0)
    Project_Name = db.Column(db.String(256), nullable = True, default = None)
    Developer_Sponsor_Co = db.Column(db.String(256), nullable = True, default = None)
    Developer_Sponsor_name = db.Column(db.String(256), nullable = True, default = None)
    Offering_Size = db.Column(db.Integer, nullable = True, default = None)
    Offering_Size_Pct_Share = db.Column(db.Integer, nullable = True, default = None)
    Total_Capital_amount = db.Column(db.Integer, nullable = True, default = None)
    Term_Months = db.Column(db.Integer, nullable = True, default = None)
    Min_Investment = db.Column(db.Integer, nullable = True, default = None)
    Fund_Underlying_security = db.Column(db.String(48), nullable = True, default = None)
    Risk_Rating = db.Column(db.String(48), nullable = True, default = None)
    Gross_Annual_Return = db.Column(db.Integer, nullable = True, default = None)
    Annual_Service_Fee = db.Column(db.Integer, nullable = True, default = None)
    Net_Return = db.Column(db.Integer, nullable = True, default = None)
    Capital_Structure = db.Column(db.Integer, nullable = True, default = None)
    Type = db.Column(db.String(48), nullable = True, default = None)
    Phase = db.Column(db.String(48), nullable = True, default = None)
    Regional_Center = db.Column(db.String(48), nullable = True, default = None)

    def __repr__(self):
        return '<Data %r>' % self.Id
    
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

