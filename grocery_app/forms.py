from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField,validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, GroceryItem, ItemCategory,User


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField(u'title', validators=[DataRequired(), Length(max=40)])
    address = StringField(u'Mailing Address', validators=[DataRequired(), validators.length(max=200)])
    submit = SubmitField(u'submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name    = StringField(u'Item Name', validators=[DataRequired()])
    price = FloatField(u'Item price',validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(min=1, max=80)])
    photo_url = StringField('Photo url', validators=[DataRequired(), URL()])
    store = QuerySelectField('store', query_factory=lambda: GroceryStore.query, allow_blank=False)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=5, max=25)])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('login')

class SignUpForm(FlaskForm):
    """ Form for new user sign up """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')