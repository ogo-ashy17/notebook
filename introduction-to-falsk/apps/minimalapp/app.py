from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook! degbug mode on ファイルを保存して再読み込みしないと画面に反映されない。せめて保存したら自動で読みんで欲しいものだが。"

# ルーティング：リクエスト先のURIと関数を紐づける
@app.route("/hello")
def hello():
    return "Hello, World!"