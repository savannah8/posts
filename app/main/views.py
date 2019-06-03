from flask import render_template,redirect,url_for,abort
from .import main
from flask_login import login_required,current_user
from .forms import CategoryForm,PostForm,CommentForm
from ..models import Category,Post,Comments,User
from .. import db
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(int(user_id))

#views
@main.route('/')
def index():
	'''
	View root page function that returns the index page and its data
	''' 
	category = Category.get_categories()
	title = "Welcome | Blog Posts"
	return render_template('index.html',title=title, category=category)

@main.route('/category/new', methods=['GET', 'POST'])    
@login_required
def profile_category():
	form = CategoryForm()
	if form.validate_on_submit():
		name = form.name.data
		profile_category = Category(name=name)
		profile_category.save_category()
		return redirect(url_for('main.index'))
	title = 'New Post Category'
	return render_template('new_category.html', category_form=form)


@main.route('/category/<int:id>')
def category(id):
    category = Category.query.get(id)
    post = Post.query.filter_by(category_id=id)

    title = f'{category.name} page'

    return render_template('category.html',title=title, category=category,post=post)

@main.route('/category/post/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_post(id):
    category = Category.query.get(id)
    form = PostForm()
    if form.validate_on_submit():
        post = form.post.data
        new_post = Post(post=post, category_id=category.id)
        new_post.save_post()
        return redirect(url_for('.category', id=category.id))

    title = 'New Post'
    return render_template('new_post.html', title=title, post_form=form, category=category)


@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get(id)
    comment = Comments.get_comments(post_id=id)

    # Comment.query.order_by(Comment.id.desc()).filter_by(pitch_id=id).all()

    title = f'Pitch { pitch.id }'
    return render_template('post.html',title=title, post=post, comment=comment)

@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    post = Post.query.get(id)
    # comment = Comment.query.get(pitch_id)

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, post_id=id)
        new_comment.save_comment()
        return redirect(url_for('.post', id=id))
    # title = f' Comment{comment.id}'
    return render_template('new_comment.html', comment_form=form, post=post)

