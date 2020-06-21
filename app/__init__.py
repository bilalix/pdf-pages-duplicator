from flask import Flask
app = Flask(__name__, static_url_path="/static")

app.config['SECRET_KEY'] = 'beep-boop'

from app import views