from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150),index=True)
    email=db.Column(db.String(150),unique=True,index=True)
    pass_secure=db.Column(db.String(100))
    blogs=db.relationship('Blogs',backref='user',lazy='dynamic')
    comments=db.relationship('Comments',backref='user',lazy='dynamic')
    code = db.Column(db.Integer,unique=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Blogs(db.Model):
    __tablename__='blogs'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    description=db.Column(db.String(250))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    @classmethod
    def delete_blog(cls,id):
        blog=Blogs.query.filter_by(id=id).first()
        db.session.delete(blog)
        db.session.commit

class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(250))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
