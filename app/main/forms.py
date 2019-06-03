from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class CategoryForm(FlaskForm):
    """
    class to create a form to create category
    """
    name = StringField('Post Category',validators=[Required()])
    submit = SubmitField('Create')


class PostForm(FlaskForm):
    """
    class to create form to write pitch
    """
    post = StringField('Post Content', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """
    class to create form to comment on a pitch
    """
    comment = StringField('Comment Content', validators=[Required()])
    submit = SubmitField('Submit')
