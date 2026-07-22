from flask import Flask, request

app = Flask(__name__)

INTERNAL_TOKEN = "internal-ops-2024"

FAKE_QUARTERLY_REPORT = {
    "quarter": "Q2-2026",
    "revenue_usd": 18_400_000,
    "unreleased_guidance_usd": 21_000_000,
    "note": "Not yet disclosed publicly — earnings call is next week.",
}


@app.route("/")
def home():
    return "Finance service is up. Requires X-Internal-Token header."


@app.route("/reports/quarterly")
def quarterly_report():
    token = request.headers.get("X-Internal-Token")
    if token != INTERNAL_TOKEN:
        return {"status": "denied", "reason": "missing or invalid X-Internal-Token"}, 403
    return {"status": "success", "report": FAKE_QUARTERLY_REPORT}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5004, debug=True)
