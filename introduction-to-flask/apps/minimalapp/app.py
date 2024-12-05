from flask import Flask, render_template, url_for, request, redirect, current_app, g

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook! degbug mode on ファイルを保存して再読み込みしないと画面に反映されない。せめて保存したら自動で読みんで欲しいものだが。"

# ルーティング：リクエスト先のURIと関数を紐づける
@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"

# show_nameエンドポイントを作成する
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # メールを送る（最後に実装）

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")