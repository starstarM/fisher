from flask import current_app, Flask


app = Flask(__name__)
a = current_app
d = current_app.config['DEBUG']