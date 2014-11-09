from flask import *

from auth.synology import is_syno_user
from utils import create_unique_token

bp = Blueprint('user', __name__, template_folder='templates')

@bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')



@bp.route('/login', methods=['POST'])
def login():

    user, password = request.form['user'], request.form['password']

    if is_syno_user(user=user, password=password):

        resp = make_response(render_template('index.html'))
        resp.set_cookie('roam_token', create_unique_token())

        redirect(url_for('index_page'))

    else:
        #TODO: Print login error msg.
        resp = make_response(render_template('login.html'))

    return resp