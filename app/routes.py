from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, SignupForm
from app.models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.validate_user(form.username.data, form.password.data)
        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        User.create_user(form.username.data, form.password.data)
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/most-visited')
def most_visited():
    places = db.places.find().sort('visits', -1).limit(5)  # Example query
    return render_template('most_visited.html', places=places)

@app.route('/cheap-cost')
def cheap_cost():
    places = db.places.find().sort('cost', 1).limit(5)  # Example query
    return render_template('cheap_cost.html', places=places)
