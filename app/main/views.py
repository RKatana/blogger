from flask import render_template,url_for,request,abort,redirect
from flask_login import login_required
from . import main
from .forms import Blog,Comment
from .. import db
from ..models import User,Blogs,Comments

@main.route('/',methods=['GET','POST'])
def index():
    blog_form=Blog()
    user = User.query.filter_by(username='uname').first()
    if blog_form.validate_on_submit():
        blogs = Blogs(title=blog_form.title.data,description=blog_form.description.data)
        db.session.add(blogs)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    def delete_blog(id):
        Blogs.delete_blog(id)
    blogs=Blogs.query.all()
    comments=Comments.query.filter_by(comment='comment').first()
    title='Home-The Blogger'
    message='The Blogger'
    return render_template('index.html',message=message,title=title,user=user,blogs=blogs,comments=comments,blog_form=blog_form,delete_blog=delete_blog)
    


@main.route('/user/<uname>', methods=['GET','POST'])
@login_required
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    blogs=Blogs.query.filter_by(user_id=user.id)
    if user is None:
        abort(404)
    title=f'{user.username}-The Blogger'
    return render_template('profile/profile.html',title=title,user=user,blogs=blogs)

@main.route('/comments/<uname>', methods=['GET','POST'])
@login_required
def comments(uname):
    form=Comment()
    if form.validate_on_submit():
        comments = Comments(comment=form.comment.data)
        db.session.add(comments)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html',form=form)