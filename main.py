from flask import Flask,render_template, jsonify

app = Flask(__name__)

SALARIES = [
  {
    "title": "Data Analyst",
    "salary": 150000
  },
   {
    "title": "Developer",
    "salary": 120000
  },
   {
    "title": "Research and developement",
    "salary": 200000,
    "remote": True
  },

]


@app.route("/")
def hello_world():
    return render_template('home.html', salaries= SALARIES)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(SALARIES)


print(__name__)

if __name__ == "__main__" :
    app.run(host= "0.0.0.0", debug=True)