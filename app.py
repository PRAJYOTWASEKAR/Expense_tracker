from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Expense
from forms import ExpenseForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        category = form.custom_category.data if form.category.data == 'Custom' else form.category.data
        expense = Expense(
            title=form.title.data,
            amount=form.amount.data,
            category=category,
            date=form.date.data
        )
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('view_expenses'))
    return render_template('add_expense.html', form=form)

@app.route('/expenses')
def view_expenses():
    expenses = Expense.query.all()
    total_expenses = sum(expense.amount for expense in expenses)
    return render_template('view_expenses.html', expenses=expenses, total_expenses=total_expenses)

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        flash('Expense deleted successfully!', 'success')
    else:
        flash('Expense not found!', 'error')
    return redirect(url_for('view_expenses'))

if __name__ == '__main__':
    app.run(debug=True)