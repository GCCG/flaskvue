from flask import Flask, render_template
app = Flask(__name__,
            static_url_path = "",
            static_folder = "./frontend/dist",
            template_folder = "./frontend/dist")
@app.route('/')
def index():
    return render_template("index.html")
