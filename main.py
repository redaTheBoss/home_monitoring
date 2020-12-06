from modules import Computer
from flask import Flask, session, request, render_template, redirect, url_for


app = Flask(__name__)
app.secret_key = 'thee'

@app.route('/', methods=['GET', 'POST'])
def index():
    
    users = {
        'username1': 'password1',
        'username2': 'password2',
    }
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            if users[username] == password:
                print('connected')
                session['connected'] = username
                return redirect(url_for('dashboard'))
            else:
                print('wrong password')
        else:
            print('wrong username')

    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html', username = session['connected'])

app.run('0.0.0.0', 80, True)




