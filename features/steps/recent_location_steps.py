from behave import *
from features.pages.home_page import HomePage


@when('I search for "{city}"')
def step_search_city(context, city):
    context.home_page.search_city(city)


@when("I click the first city in recent locations")
def step_click_first_recent(context):
    context.home_page.click_first_recent_result()


@then("I should see the city name from recent locations in the page header")
def step_verify_city_header(context):
    context.home_page.get_page_header()
