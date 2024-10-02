from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.set_viewport_size({"width":1920,"height":1080}) # Assuning a common screen resolution

page.goto("https://magento.softwaretestingboard.com/")

input("end")