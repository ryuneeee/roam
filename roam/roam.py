import logging

from flask import Flask, render_template, session, url_for, redirect
from sqlalchemy import create_engine

from web.controllers import login
from models import Base
import settings




# SQLAlchemy & Model binding
engine = create_engine('sqlite:///')
Base.metadata.create_all(engine)


# TODO: make logger class using yaml conf.
# ref: https://docs.python.org/3.4/library/logging.config.html#dictionary-schema-details
# Logging module
logging.basicConfig(format=settings.LOGGING_FORMAT, level=settings.LOGGING_LEVEL)

# Flask
app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

# Flask Blueprint
app.register_blueprint(login.bp)


@app.route('/')
def index_page():
    if session.get('user') is None:
        return redirect(url_for('login.login_page'))
    else:
        return render_template('index.html', title=settings.ROAM_NAME)

@app.route('/logout')
def clear():
    session['user'] = None
    return redirect(url_for('index_page'))

app.run(host=settings.ROAM_HOST, port=settings.ROAM_PORT,
        use_reloader=True, use_debugger=True, debug=True)