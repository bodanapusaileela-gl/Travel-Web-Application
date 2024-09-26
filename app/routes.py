from flask import render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash
from app import app, db
from datetime import datetime
from werkzeug.security import check_password_hash

#from app.forms import LoginForm, SignupForm,  # Import your LoginForm and SignupForm

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email
        user = db.users.find_one({'email': email})

        if user:
            # Check if the password matches
            if check_password_hash(user['password'], password):  # Now check_password_hash is defined
                # Store user session
                session['user_id'] = str(user['_id'])
                session['username'] = user['username']
                flash(f"Welcome back, {user['username']}!", "success")
                return redirect(url_for('home'))
            else:
                flash("Invalid password", "danger")
        else:
            flash("Email not found", "danger")

    return render_template('login.html')

'''@app.route('/login', methods=['GET', 'POST'])
#def login():
  #  if request.method == 'POST':
 #       # Get form data
   #     email = request.form.get('email')
    #    password = request.form.get('password')

        # Find user by email
     #   user = db.users.find_one({'email': email})

        if user:
            # Check if the password matches
            if check_password_hash(user['password'], password):
                # Store user session
                session['user_id'] = str(user['_id'])
                session['username'] = user['username']
                flash(f"Welcome back, {user['username']}!", "success")
                return redirect(url_for('home'))
            else:
                flash("Invalid password", "danger")
        else:
            flash("Email not found", "danger")

    return render_template('login.html'
    '''
# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check if password and confirm password match
        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return redirect(url_for('signup'))

        # Check if username or email already exists
        if db.users.find_one({'email': email}):
            flash("Email is already registered", "danger")
            return redirect(url_for('signup'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert user into MongoDB
        user_data = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'created_at': datetime.utcnow()
        }
        db.users.insert_one(user_data)

        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for('login'))

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
#Route logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out", "info")
    return redirect(url_for('login'))
