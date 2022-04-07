# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileField, FileRequired




class UploadForm(FlaskForm):
    description = TextAreaField(
        name='description',
        label='Description',
        validators=[InputRequired()]
    )
    
    photo = FileField(
        name='photo',
        label='Photo',
        validators=[FileAllowed(['jpg', 'png']), FileRequired()]
    )