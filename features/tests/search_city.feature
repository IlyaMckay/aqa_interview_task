Feature: Search for the NYC on AccuWeather

  Scenario: Search for "New York" and check if it is matches the page header
    Given I open the AccuWeather home page
    When I search for "New York" 
    And The search results list is displayed
    And I click the first search result
    Then I should see the city name "New York" in the page header
