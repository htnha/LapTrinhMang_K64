from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless=True for headless mode
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())  # Prints the title of the page
    browser.close()

with sync_playwright() as playwright:
    run(playwright)