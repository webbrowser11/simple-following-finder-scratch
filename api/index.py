from flask import Flask, render_template, request
import scratchattach as sa

app = Flask(__name__, template_folder="../templates")

@app.route("/static/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        user_input = request.form.get("my_input")
        try:
            user = sa.get_user(user_input)
            user_input = user.following_count()
        except Exception as e:
            user_input = f"User does not exist or another error."
        output = f"{user_input}"
    return render_template("index.html", output=output)


