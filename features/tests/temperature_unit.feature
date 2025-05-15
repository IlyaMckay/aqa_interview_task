Feature: Temperature measurement units change

  Scenario: Go to the settings, change measurement units, go back, check if units changed
    Given I open the AccuWeather home page
    When I click hamburger menu button
    And I check if the settings page is dispalyed
    And I click settings button
    And I change C to F
    And I go back to the main page using browser navigation
    Then I check if the temperature is indicated in F
