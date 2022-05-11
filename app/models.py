from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app import db, login_manager
from flask_login import UserMixin
# from . import views,forms



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
   
    def _repr_(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def _repr_(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    pitch = db.Column(db.String(255))
    category = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref='pitch',lazy="dynamic")
    upvotes = db.relationship('Upvote',backref='pitch',lazy="dynamic")
    downvotes = db.relationship('Downvote',backref='pitch',lazy="dynamic")
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