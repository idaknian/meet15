from flask_login import UserMixin

from application import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(128))
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    pp = db.Column(db.String(128), default="default.jpg")
    status = db.Column(db.Boolean, default=True)
    following_users = db.relationship("Relationship", foreign_keys="Relationship.id_following", backref="following", lazy=True)
    follower_users = db.relationship("Relationship", foreign_keys="Relationship.id_follower", backref="follower" lazy=True)
    posts = db.relationship("Post" backref="posts_owner", lazy=True)
    comments = db.relationship("Comment" backref="comments_owner" lazy=True)
    likes = db.relationship("Like" backref="likes_owner" lazy=True)

class Relationship(db.Model):
    __tablename__ = 'relationship'
    id = db.Column(db.Integer, primary_key=True)
    id_followers = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    id_following = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    relation_date = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(128), nullable=False)
    caption = db.Column(db.String(128), default="")
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    author.id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    comments = db.relationship("Comment" backref="commented" lazy=True)
    likes = db.relationship("Like" backref="liked" lazy=True)

class Comment(Db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable = False)
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.id"), priamary_key = True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    hidden = db.Column(db.Boolean, default=False)

class Like(db.Model):
    __tablename__ = 'like'
    id = db.Column(db.Integer, primary_key=True)
    like_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, default=datetime.utcnow)