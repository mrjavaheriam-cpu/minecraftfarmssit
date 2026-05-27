from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'ye ketabe asrare amigh'
PASSWORD = "minecraft"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = 'رمز اشتباهه! دوباره تلاش کن.'
    return render_template('login.html', error=error)

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/makefarm/')
@login_required        
def jozve():
    return render_template('makefarm.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)