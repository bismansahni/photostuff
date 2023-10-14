from flask import Flask, request, render_template, session, redirect, url_for
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy database for user data
users = {
    'username1': {
        'password': 'hashed_password1',
        'image_hash': 'hashed_image_data1'
    },
    'username2': {
        'password': 'hashed_password2',
        'image_hash': 'hashed_image_data2'
    }
}

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        image_hash = hashlib.sha256(request.form['image'].read()).hexdigest()
        users[username] = {'password': password, 'image_hash': image_hash}
        return redirect('/login')
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        if username in users and users[username]['password'] == password:
            session['authenticated'] = True
            return redirect('/dashboard')
    return render_template('login.html')

# Route for the dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('authenticated'):
        return redirect('/login')
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
