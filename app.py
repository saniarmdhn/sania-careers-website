from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
   { "id" : 1,
    "title": "Data Analyst" ,
    "location": "Bengluru, India",
    'salary' : "Rs. 12,00,000"},

    { "id" : 2,
    "title": "FE",
    "location": "remote",
    'salary' : "Rs. 15,00,000"},

    { "id" : 3,
    "title": "BE",
    "location": "San Fransisco, USA",
    'salary' : "Rs. 13,00,000"},

    { "id" : 4,
    "title": "QA engineer",
    "location": "Remote",
    'salary' : "Rs. 15,00,000"}
    

    ]

@app.route("/")
def hello_world():
    return render_template('home.html',
                            jobs=JOBS,
                            company_names = 'sania')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
