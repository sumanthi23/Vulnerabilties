from flask import Flask

app = Flask(__name__)

FAKE_EMPLOYEES = [
    {"id": 101, "name": "D. Whitfield", "role": "VP Engineering", "salary": 241000, "ssn_last4": "7734"},
    {"id": 102, "name": "N. Okafor", "role": "Staff Engineer", "salary": 198500, "ssn_last4": "2210"},
    {"id": 103, "name": "L. Marchetti", "role": "Finance Director", "salary": 205000, "ssn_last4": "8891"},
    {"id": 104, "name": "P. Andresen", "role": "HR Manager", "salary": 132000, "ssn_last4": "0043"},
]


@app.route("/")
def home():
    return "HR service is up."


@app.route("/employees")
def employees():
    return {"status": "success", "employees": FAKE_EMPLOYEES}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=True)
