from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class ExpenseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
        ('Custom', 'Custom')  # Option for custom input
    ])
    custom_category = StringField('Custom Category')  # Field for custom category input
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Expense')