import json
from datetime import datetime
from playwright.sync_api import sync_playwright

def fetch_sofascore_today():
    # Get today's date (YYYY-MM-DD)
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.sofascore.com/api/v1/sport/football/scheduled-events/{today}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")

        # Extract JSON text
        content = page.inner_text("pre")
        data = json.loads(content)

        # Always save as mapi.json
        with open("mapi.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Today's data ({today}) saved successfully to mapi.json")
        browser.close()
        return data

# Run
if __name__ == "__main__":
    fetch_sofascore_today()
