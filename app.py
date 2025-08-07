from flask import Flask, render_template,  request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash
# ---------------------- Config ---------------------- #
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ---------------------- DB Init --------------------- #
db = SQLAlchemy(app)

# ---------------------- Models ---------------------- #
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"
    
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    course = db.Column(db.String(120), nullable=False)
    payment_id = db.Column(db.String(120))  # Optional, for Razorpay payment ID

    def __repr__(self):
        return f"Enrollment('{self.name}', '{self.course}')"

# ---------------------- Routes ---------------------- #
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/baking')
def baking():
    return render_template('baking.html')

@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/better')
def better():
    return render_template('better.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    email = request.form['email']
    subject = request.form['subject']
    description = request.form['description']
    file = request.files.get('file')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Add authentication logic here
        flash (f"Logged in as: {email}")
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            flash("❌ Passwords do not match.")
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("⚠️ Email already registered. Please login or use another email.")
            return redirect(url_for('register'))

        try:
            hashed_password = generate_password_hash(password)
            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("✅ Account created successfully. Please login.")
            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()
            flash("❌ An error occurred. Please try again later.")
            print("Register Error:", e)

    return render_template('register.html')
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')
        payment_id = request.form.get('razorpay_payment_id')  # Optional

        # Save to database
        enrollment = Enrollment(name=name, email=email, course=course, payment_id=payment_id)
        db.session.add(enrollment)
        db.session.commit()

        flash("✅ Enrollment successful! Welcome, {}".format(name))
        return redirect(url_for('home'))
    return render_template('enroll.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
