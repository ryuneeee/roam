from flask import Flask, render_template, session, url_for, redirect
from controllers import login
import settings

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

app.register_blueprint(login.bp)


@app.route('/')
def index_page():
    if session.get('user') is None:
        return redirect(url_for('login.login_page'))
    else:
        return render_template('index.html', box_name=settings.ROAM_NAME)

@app.route('/logout')
def clear():
    session['user'] = None
    return redirect(url_for('index_page'))

app.run(host=settings.ROAM_HOST, port=settings.ROAM_PORT,
        use_reloader=True, use_debugger=True, debug=True)