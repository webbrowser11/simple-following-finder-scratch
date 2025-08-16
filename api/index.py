from flask import Flask, render_template, request
import scratchattach as sa
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        user_input = request.form.get("my_input")
        try:
            user = sa.get_user(user_input)
            user_input = user.following_count()
        except Exception as e:
            user_input = "User does not exist or another error."
        output = f"You typed: {user_input}"
    return render_template("index.html", output=output)

# For Vercel: expose app as "handler"
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# For running locally (optional)
if __name__ == "__main__":
    run_simple("0.0.0.0", 5000, app)