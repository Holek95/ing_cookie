from behave import given, when, then
from features.page.ing_landing_page import IngLandingPage


@given("użytkownik jest na stronie startowej")
def step_open_home_page(context):
    context.page = context.browser.new_page()
    context.ing_page = IngLandingPage(context.page)
    context.ing_page.navigate_to_home_page()

@when("użytkownikowi wyświetla się okno wyboru cieasteczek")
def step_click_cookie_settings(context):
    context.ing_page.click_adjust_cookies_button()

@when("użytkownik akceptuje ciasteczka analityczne")
def step_enable_analytics(context):
    context.ing_page.enable_analytical_cookies_if_disabled()

@when("użytkownik akceptuje zaznaczone zgody")
def step_accept_selected(context):
    context.ing_page.accept_selected_cookie_settings()

@then("ciasteczka, w tym analityczne, są zapisane")
def step_verify_cookie(context):
    context.ing_page.verify_analytical_cookie_consent_saved()
    context.page.close()
