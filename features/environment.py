from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()


def before_feature(context, feature):
    context.browser = context.playwright.firefox.launch(
        headless=True,
        args=["--disable-http2"]
    )
    browser_context = context.browser.new_context(
        viewport={"width": 1280, "height": 720},
        user_agent="Mozilla/5.0 (Windows NT 10.0: Win64; x64) AppleWebKit/537.36 \ (KHTML, Like Gecko) Chrome/113.0.0.0 Safari/537.36"
    )
    context.page = browser_context.new_page()


def after_feature(context, feature):
    context.page.close()
    context.browser.close()


def after_all(context):
    context.playwright.stop()
