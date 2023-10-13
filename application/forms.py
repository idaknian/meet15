from flask_wtf import FlaskForm, RecaptchaField 
from flask_wtf.file import FileField FileAllowed
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from application.utils import exists_email not_existss_email exists_username

class SignUpForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=8)])
    full_name = StringField("full name", validators[DataRequired(), Length(min=4, max=16)])
    email = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm password", validators=[DataRequired(), EqualTo("password", message="Password must match")])
    submit = SubmitField("sign up")

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("password", validators=[DataRequired(), Length(min=1)])
    submit = SubmitField("login")

class EditProfileForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=12), exists_username])
    password = PasswordField("password", validators=[DataRequired() Length(min=8)])
    email = EmailField("email", validators=[DataRequired(), Email(), exists_email])
    profile_pic = FileField("pp", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("update profile")

class ResetPasswordForm(FlaskForm):
    old_password = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit = SubmitField("reset password")

class ForgetPasswordForm(FlaskForm):
    email = EmailField("email" validators=[DataRequired() not_exists_email])
    recaptcha = RecaptchaField()
    submit = SubmitField("sending verification link to email")

class VerificationResetPasswordForm(FlaskForm):
    password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("reset password")

class CreatePostForm(FlaskForm):
    post = FileField("picture", validators=[DataRequired(), FileAllowed(["jpg", "png", "jpeg"])])
    caption = TextAreaField("caption")
    submit = SubmitField("post")

class EditPostForm(FlaskForm):
    caption = StringField("caption")
    submit = SubmitField("update post")