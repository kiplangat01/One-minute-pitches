from datetime import datetime
from flask import current_app
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from . import views,forms



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
   
    def _repr_(self):
        return f"User('{self.username}', '{self.email}', '{self.password}' '{self.image_file}')"
    
class Post(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    
    def _repr_(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    pitch = db.Column(db.String(255))
    category = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.column(db.String(255))
    upvotes = db.Column(db.Integer())
    downvotes = db.Column(db.Integer())
    def __init__(self,title,pitch,category,upvotes,downvotes,comments):
         self.title = title
         self.pitch = pitch
         self.category = category
         self.upvotes = upvotes
         self.downvotes = downvotes
         self.comments = comments
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches
    def __repr__(self):
        return f'Pitch {self.pitch}'

