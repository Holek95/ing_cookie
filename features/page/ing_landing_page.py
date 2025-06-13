from playwright.sync_api import Page

class IngLandingPage:
    URL = "https://www.ing.pl/"
    ADJUST_BUTTON = 'text="Dostosuj"'
    ANALYTICAL_TOGGLE = 'div[name="CpmAnalyticalOption"]'
    ACCEPT_BUTTON = 'button:has-text("Zaakceptuj zaznaczone")'
    COOKIE_NAME_TO_VERIFY = "cookiePolicyGDPR"
    EXPECTED_COOKIE_VALUE = "3"

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_home_page(self):
        self.page.goto(self.URL)

    def click_adjust_cookies_button(self):
        self.page.wait_for_selector(self.ADJUST_BUTTON, timeout=10000).click()

    def enable_analytical_cookies_if_disabled(self):
        analytical_toggle = self.page.locator(self.ANALYTICAL_TOGGLE)
        analytical_toggle.wait_for()

        if analytical_toggle.get_attribute("aria-checked") == "false":
            analytical_toggle.click()

    def accept_selected_cookie_settings(self):
        self.page.click(self.ACCEPT_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def verify_analytical_cookie_consent_saved(self):
        cookies = self.page.context.cookies()
        found = any(
            self.COOKIE_NAME_TO_VERIFY in cookie['name'] and cookie['value'] == self.EXPECTED_COOKIE_VALUE
            for cookie in cookies
        )
        assert found