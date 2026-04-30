from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='OVERVIEW OF SUBPAGES')

@app.route('/register')
def register():
    return '''
        <h1> Register </h1>
    '''

@app.route('/login')
def login():
    return '''
        <h1> Login </h1>
    '''

@app.route('/delete')
def delete():
    return '''
        <h1> Delete </h1>
    '''

@app.route('/captcha')
def captcha():
    return '''
        <h1> Captcha </h1>
    '''