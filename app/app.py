# -*- coding: utf-8 -*-

from flask import render_template, request, Flask

from app.database import init_db
from app.models import Post
from app.forms import PostForm
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    return app

app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = PostForm(request.form)
        if form.validate_on_submit():
            post = Post()
            post.name = form.name.data
            post.body = form.body.data
            post.title = form.title.data

            db.session.add(post)
            db.session.commit()

    posts = Post.query.all()

    form = PostForm()
    return render_template(
        'top.html',
        posts=posts,
        form=form,
    )



if __name__ == '__main__':
    app.run()
