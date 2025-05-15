from behave import *
from features.pages.home_page import HomePage


@when('I click hamburger menu button')
def step_click_hamburger_button(context):
    context.home_page.click_hamburger_button()

@when('I check if the settings page is dispalyed')
def step_check_settings_page_is_visible(context):
    context.home_page.settings_page_is_visible()

@when('I click settings button')
def step_click_settings(context):
    context.home_page.click_settings_button()

@when("I change C to F")
def step_change_measurements(context):
    context.home_page.change_c_to_f()

@then("I check if the temperature is indicated in F")
def step_check_weater_unit(context):
    context.home_page.check_if_weather_unit_is_f()