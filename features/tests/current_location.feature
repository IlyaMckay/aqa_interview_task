Feature: Search for the weather by the current location on AccuWeather

  Scenario: Search for the weather in the city where I am
    Given I open the AccuWeather home page
    When I click the search bar
    Then I should see the "Use your current location" label is displayed
