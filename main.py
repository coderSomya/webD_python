from flask import Flask,render_template

app = Flask(__name__)

SALARIES = [
    "1L", "2L", "3L", "1L", "1.5"
]


@app.route("/")
def hello_world():
    return render_template('home.html', salaries= SALARIES)


print(__name__)

if __name__ == "__main__" :
    app.run(host= "0.0.0.0", debug=True)