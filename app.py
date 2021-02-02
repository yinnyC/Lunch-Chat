# ------------------------------------
# Import the Libraries
# ------------------------------------
from flask import Flask, render_template, request
# ------------------------------------
# Declare Variables and Instances
# ------------------------------------
app = Flask(__name__)  # Instantiate the Flask class

# ------------------------------------
# Define Functions for Routes
# ------------------------------------


@app.route('/')
def homepage():
    """Return index template."""
    sth = "hello world"
    return render_template('index.html', sth=sth)


if __name__ == '__main__':
    app.run(debug=True)
