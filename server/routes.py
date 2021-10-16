from server import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Sign/Up')
def signup():
    return render_template('sign_up.html')

@app.route('/Sign/In')
def signin():
    return render_template('sign_in.html')
