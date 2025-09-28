import json
from datetime import datetime
from flask import Flask, Response
from playwright.sync_api import sync_playwright

app = Flask(__name__)

def fetch_sofascore_today():
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.sofascore.com/api/v1/sport/football/scheduled-events/{today}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")
        content = page.inner_text("pre")
        data = json.loads(content)
        browser.close()
        return data

@app.route("/mapi.json")
def serve_json():
    data = fetch_sofascore_today()
    return Response(
        json.dumps(data, indent=2, ensure_ascii=False),
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
