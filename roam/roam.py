from flask import Flask, render_template
from controllers import user

app = Flask(__name__)

app.register_blueprint(user.bp)


@app.route('/')
def index_page():
    return render_template('index.html')

app.run(port=8000, debug=False)