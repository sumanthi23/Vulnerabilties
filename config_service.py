from flask import Flask

app = Flask(__name__)

FAKE_CONFIG = {
    "stripe_api_key": "sk_live_FAKEKEYDONOTUSE00000000",
    "sendgrid_api_key": "SG.fake_example_key_do_not_use",
    "database_url": "postgres://svc_app:fake-pw-example@db-internal.local:5432/shopstock",
    "jwt_signing_secret": "fake-signing-secret-do-not-use",
}


@app.route("/")
def home():
    return "Config service is up."


@app.route("/config")
def config():
    return FAKE_CONFIG


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)
