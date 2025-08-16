from flask import Flask, render_template, request
import scratchattach as sa

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
            user_input = "error: {e}"
        output = user_input
    return render_template("index.html", output=output)

# Expose handler for Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

