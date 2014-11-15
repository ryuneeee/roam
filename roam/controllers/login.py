from flask import *

from auth.synology import is_syno_user
import settings

bp = Blueprint('login', __name__, template_folder='templates')


def is_local_test(user, password):
    return request.remote_addr == '127.0.0.1' and user == 'user' and password == 'pw'


@bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html',
                           title=settings.ROAM_NAME,
                           hero=settings.ROAM_NAME)


@bp.route('/login', methods=['POST'])
def login():
    user, password = request.form.get('user', None), request.form.get('password', None)

    if not user or not password:
        return render_template('login.html',
                               title=settings.ROAM_NAME,
                               hero=settings.ROAM_NAME,
                               msg='Please input\n Username and Password.'), 404

    elif is_local_test(user, password) or is_syno_user(user, password):
        session['user'] = user
        return redirect(url_for('index_page'))

    else:
        return render_template('login.html',
                               title=settings.ROAM_NAME,
                               hero=settings.ROAM_NAME,
                               msg='Invalid Username or Password.')