from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook! degbug mode on ファイルを保存して再読み込みしないと画面に反映されない。せめて保存したら自動で読みんで欲しいものだが。"

# ルーティング：リクエスト先のURIと関数を紐づける
@app.route("/hello/<int:name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"

# show_nameエンドポイントを作成する
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)