from flask_wtf import FlaskForm
from ..models import User
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,ValidationError,SelectField
from wtforms.validators import DataRequired, Email,EqualTo


# creating user account
class Signup_form(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('confirm', validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')



# user login
class login_form(FlaskForm):
    Email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title')
    pitch = TextAreaField('write your pitch here')
    category = SelectField('Choose your prefered category',choices=[('health','health'), ('comedy','comedy'), ('business','business')])
    submit = SubmitField('Pitch')
class CommentForm(FlaskForm):
    comment = TextAreaField('write your comment here')
    submit = SubmitField('Pitch')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')