from flask import Flask, request

app = Flask(__name__)

VALID_ACCESS_KEY = "AKIAFAKEEXAMPLE00"
VALID_SECRET_KEY = "fake/secret/do-not-use/1234567890abcd"

FAKE_CUSTOMER_RECORDS = [
    {"id": 1, "name": "A. Example", "ssn_last4": "1234", "card_last4": "4242"},
    {"id": 2, "name": "B. Sample", "ssn_last4": "5678", "card_last4": "1881"},
    {"id": 3, "name": "C. Testcase", "ssn_last4": "9012", "card_last4": "9001"},
]


@app.route("/")
def home():
    return "Vault service is up. Requires X-Access-Key-Id / X-Secret-Access-Key headers."


@app.route("/buckets/customer-data")
def customer_data():
    access_key = request.headers.get("X-Access-Key-Id")
    secret_key = request.headers.get("X-Secret-Access-Key")

    if access_key == VALID_ACCESS_KEY and secret_key == VALID_SECRET_KEY:
        return {"status": "success", "records": FAKE_CUSTOMER_RECORDS}

    return {"status": "denied", "reason": "invalid or missing credentials"}, 403


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)
