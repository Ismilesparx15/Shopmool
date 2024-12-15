import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """Set up the Playwright instance."""
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Set up the browser."""
    browser = playwright_instance.chromium.launch(headless=False)  # Set headless=True for headless mode
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def setup(browser):
    """Set up a new browser context and page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
