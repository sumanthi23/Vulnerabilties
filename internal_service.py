from flask import Flask, request, redirect

app = Flask(__name__)

FAKE_ADMIN_SECRET = "FLAG{internal_admin_panel_reached_via_ssrf}"

FAKE_IAM_CREDENTIALS = {
    "Code": "Success",
    "Type": "AWS-HMAC",
    "AccessKeyId": "AKIAFAKEEXAMPLE00",
    "SecretAccessKey": "fake/secret/do-not-use/1234567890abcd",
    "Token": "fake-session-token",
    "Expiration": "2099-01-01T00:00:00Z",
}


@app.route("/")
def home():
    return "Internal service is up."


@app.route("/admin/secret")
def admin_secret():
    return {"status": "success", "secret": FAKE_ADMIN_SECRET}


@app.route("/latest/meta-data/iam/security-credentials/")
def metadata_role_list():
    return "ISRM-WAF-Role"


@app.route("/latest/meta-data/iam/security-credentials/<role>")
def metadata_role_creds(role):
    return FAKE_IAM_CREDENTIALS


@app.route("/redirect")
def open_redirect():
    target = request.args.get("url", "/admin/secret")
    return redirect(target, code=302)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
