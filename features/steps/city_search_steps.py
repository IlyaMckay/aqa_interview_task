from behave import *
from features.pages.home_page import HomePage


@when('The search results list is displayed')
def step_verify_results_list_is_visible(context):
    context.home_page.results_list_is_visible()


@then('I should see the city name "{city}" in the page header')
def step_verify_city_header(context, city):
    header = context.home_page.get_page_header()
    assert (city.lower() in header.lower()), f"Expected city '{city}' in header, but got '{header}'"
