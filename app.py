from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def program():
    return render_template('index.html')


@app.route('/contato', methods=["GET", "POST"])
def contato():
    return render_template('contato.html')


if __name__ == "__main__":
    app.run(debug=True)
