from flask

app = Flask(__name__)

@app.route("/")
def init():
    return flask.render_template("index.html", token="Hello Flask+React")

@app.route("/login")
def login():
    return 'login'

@app.route("/user/<username>")
def profile(username):
    return '{}\'s profile'.format(username)

@app.route("/bowling")
def bowling_index():
    return 'Hello \n <h1>Bowling Page</h1>'

app.run(debug=True)