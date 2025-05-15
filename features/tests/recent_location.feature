Feature: Search for a city on AccuWeather

  Scenario: Search for "London", open the first result, go back, open the first city in recent locations
    Given I open the AccuWeather home page
    When I search for "London"
    And I click the first search result
    And I go back to the main page using browser navigation
    And I click the first city in recent locations
    Then I should see the city name from recent locations in the page header
