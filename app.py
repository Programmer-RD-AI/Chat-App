from flask import *
app = Flask(__name__)
app.secret_key = 'YERYRE'
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['NAME']
        password = request.form['PASSWORD']
        session['Password'] = password
        session['Name'] = name
        print(name,password)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
