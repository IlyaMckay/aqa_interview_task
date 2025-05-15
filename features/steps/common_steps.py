from behave import *
from features.pages.home_page import HomePage


@given("I open the AccuWeather home page")
def step_open_home(context):
    context.home_page = HomePage(context.page)
    context.home_page.load_and_consent()


@when("I click the first search result")
def step_click_first_result(context):
    context.home_page.click_first_result()


@when("I go back to the main page using browser navigation")
def step_go_back(context):
    context.home_page.click_back_button()
