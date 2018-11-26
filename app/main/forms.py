from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required
from ..models import Blogs

class Blog(FlaskForm):
    title= StringField('Enter title',validators=[Required()])
    description=TextAreaField('Add your blog',validators=[Required()])
    submit=SubmitField('Submit')

class Comment(FlaskForm):
    comment=TextAreaField('Enter your comment',validators=[Required()])
    submit=SubmitField('Submit')
