from flask import render_template, redirect, url_for, request, flash
from app import app
from app.forms import LoginForm  # Import your LoginForm

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Create an instance of the LoginForm
    if request.method == 'POST' and form.validate_on_submit():
        # Here you would add logic to check username and password
        # For example, check against a database or a predefined list
        username = form.username.data
        password = form.password.data
        # Add your authentication logic here
        if username == 'admin' and password == 'password':  # Replace with actual authentication
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to home on successful login
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    return render_template('login.html', form=form)  # Pass the form to the template

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Logic for handling signup (you'll need to add this)
        pass
    return render_template('signup.html')

# Route for the services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the cheap_cost page
@app.route('/cheap-cost')
def cheap_cost():
    places = [
        {"name": "Bali", "location": "Indonesia", "cost": 500},
        {"name": "Phuket", "location": "Thailand", "cost": 400},
        {"name": "Goa", "location": "India", "cost": 300}
    ]
    return render_template('cheap_cost.html', places=places)

# Route for the most_visited page
@app.route('/most-visited')
def most_visited():
    places = [
        {"name": "Paris", "location": "France", "visits": 12000},
        {"name": "New York", "location": "USA", "visits": 9000},
        {"name": "Tokyo", "location": "Japan", "visits": 8000}
    ]
    return render_template('most_visited.html', places=places)

