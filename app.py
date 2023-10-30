from flask import Flask, render_template

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', methods=["GET", "POST"])
=======
@app.route('/')
>>>>>>> 44a1a029602b4e9923c1466ed084d07791e55ab6
def program():
    return render_template('index.html')


<<<<<<< HEAD
@app.route('/contato', methods=["GET", "POST"])
=======
@app.route('/contato')
>>>>>>> 44a1a029602b4e9923c1466ed084d07791e55ab6
def contato():
    return render_template('contato.html')


if __name__ == "__main__":
    app.run(debug=True)
