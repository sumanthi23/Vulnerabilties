import json
import time
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

TRUSTED_TOKEN = "cdn.shopstock.local"


def naive_whitelist_check(url: str) -> bool:
    return TRUSTED_TOKEN in url


@app.route("/")
def catalog():
    return render_template("catalog.html", title="Catalog · ShopStock", active="catalog")


@app.route("/orders")
def orders():
    return render_template("orders.html", title="Orders · ShopStock", active="orders")


@app.route("/vendors")
def vendors():
    return render_template("vendors.html", title="Vendors · ShopStock", active="vendors")


@app.route("/settings")
def settings():
    return render_template("settings.html", title="Settings · ShopStock", active="settings")


@app.route("/import-image")
def import_image():
    url = request.args.get("url")
    result = None
    flagged = False

    if url:
        if not naive_whitelist_check(url):
            result = "Import failed: this source isn't on our approved CDN list."
        else:
            try:
                resp = requests.get(url, timeout=3)
                try:
                    data = resp.json()
                    if isinstance(data, dict) and "AccessKeyId" in data and "SecretAccessKey" in data:
                        flagged = True
                        vault_resp = requests.get(
                            "http://127.0.0.1:5002/buckets/customer-data",
                            headers={
                                "X-Access-Key-Id": data["AccessKeyId"],
                                "X-Secret-Access-Key": data["SecretAccessKey"],
                            },
                            timeout=3,
                        )
                        result = json.dumps(data, indent=2) + "\n\n" + vault_resp.text
                    else:
                        result = resp.text[:2000]
                except ValueError:
                    result = f"[{resp.status_code}] {len(resp.content)} bytes, content-type: {resp.headers.get('content-type', 'unknown')}"
            except Exception as e:
                result = f"error: {e}"

    return render_template("catalog.html", title="Catalog · ShopStock", active="catalog",
                            submitted_url=url, result=result, flagged=flagged)


@app.route("/test-webhook")
def test_webhook():
    url = request.args.get("url")
    header_name = request.args.get("header_name")
    header_value = request.args.get("header_value")
    result = None
    elapsed_ms = None
    if url:
        headers = {}
        if header_name and header_value:
            headers[header_name] = header_value
        start = time.monotonic()
        try:
            resp = requests.get(url, headers=headers, timeout=2)
            result = f"Connection succeeded (HTTP {resp.status_code})."
            if resp.status_code == 200 and resp.text.strip():
                result += f" Response snippet: {resp.text[:300]}"
        except requests.exceptions.Timeout:
            result = "Timed out."
        except requests.exceptions.ConnectionError:
            result = "Connection refused."
        except Exception as e:
            result = f"Error: {e}"
        elapsed_ms = round((time.monotonic() - start) * 1000)
    return render_template("settings.html", title="Settings · ShopStock", active="settings",
                            webhook_url=url, webhook_result=result, webhook_ms=elapsed_ms,
                            header_name=header_name, header_value=header_value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
