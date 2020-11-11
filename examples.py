from flask import Flask, render_template
from main import FlaskInform, Attention

class PasswordIsNotCorrect(FlaskInform):
    m: 'Password is incorrect'
    # l: 'danger' by default

class Unauthorized(FlaskInform):
    m: 'Login is required'
    l: Attention.warning

class LoginSuccess(FlaskInform):
    m: 'You successfully logged in'
    l: Attention.success

app = Flask(__name__, template_folder='.')
app.secret_key = 'secret'

@app.route('/if-you-catch')
def a():
    try:
        raise Unauthorized
    except Exception as e:
        e.flash() # Equivalent to flash('Login is required', 'warning')
    return render_template('template.htm')

@app.route('/if-you-catch-with-argument')
def b():
    try:
        raise Unauthorized
    except Exception as e:
        e.flash('go to /login') # Equivalent to flash('Login is required: go to /login', 'warning')
    return render_template('template.htm')

@app.route('/you-may-not-instantiate-a-class-to-flash')
def c():
    PasswordIsNotCorrect.flash() # Equivalent to flash('Password is incorrect, 'danger')
    return render_template('template.htm')

@app.route('/success-example')
def d():
    username = 'phantie'
    LoginSuccess.flash(username) # Equivalent to flash('You successfully logged in: phantie', 'success')
    return render_template('template.htm')

if __name__ == "__main__":
    app.run()