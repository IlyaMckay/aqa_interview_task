Feature: Settings page

    Scenario: User should open the Accuweather settings page
        Given Accuweather settings page
        When User sees the "Units" dropdown list
        Then User changes "Metric" to "Imperial" measure system