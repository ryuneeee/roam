from flask import *

from auth.synology import is_syno_user
from test.fake_syno_shell import FakeSyno

bp = Blueprint('user', __name__, template_folder='templates')


@bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login():
    user, password = request.form['user'], request.form['password']

    if is_syno_user(user=user, password=password):
        session['user'] = user

        return redirect(url_for('index_page'))

    else:
        # TODO: Print login error msg.
        resp = make_response(render_template('login.html'))

    return resp