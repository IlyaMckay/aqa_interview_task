from behave import *
from features.pages.home_page import HomePage


@when("I click the search bar")
def step_click_search(context):
    context.home_page.click_search_bar()


@then('I should see the "Use your current location" label is displayed')
def step_verify_label_is_displayed(context):
    context.home_page.location_label_is_visible()
