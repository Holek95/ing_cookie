import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.context.clear_cookies()
    yield page
    page.close()


def test_ing_privacy_settings(page):
    page.goto("https://www.ing.pl/")

    # Poczekaj na przycisk "Dostosuj" i kliknij
    page.wait_for_selector('text="Dostosuj"', timeout=10000)
    page.click('text="Dostosuj"')

    # Zaznacz zgode na analityczne ciasteczka, jeśli nie są już zaznaczone
    analytical_toggle = page.locator('div:has-text("Cookies")').filter(has_text="analityczne").locator('div[name="CpmAnalyticalOption"]')
    analytical_toggle.wait_for()

    if analytical_toggle.get_attribute("aria-checked") == "false":
        analytical_toggle.click()

    # Akceptuj zaznaczone ustawienia
    page.click('button:has-text("Zaakceptuj zaznaczone")')

    # Poczekaj na zapis cookies
    page.wait_for_load_state("networkidle")

    # Sprawdź, czy cookies zostały zapisane
    cookies = page.context.cookies()
    found = any(
        "cookiePolicyGDPR" in cookie['name'] and cookie['value'] == "3"
        for cookie in cookies
    )
    assert found, "Nie znaleziono potwierdzenia zgody w cookie."
    print("Zgoda analityczna została poprawnie zapisana.")

