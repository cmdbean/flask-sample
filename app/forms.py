# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('投稿者', validators=[DataRequired()])
    title = StringField('件名', validators=[DataRequired()])
    body = TextAreaField('本文', validators=[DataRequired()])
