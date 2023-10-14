from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# A list to store registration data (in-memory storage, not suitable for production)
registration_data = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        image = request.files['image']

        # You can process and store the data as needed here
        # For simplicity, we'll just store it in a list
        registration_data.append({'username': username, 'password': password, 'image': image.filename})

        # Redirect to a success page
        return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
