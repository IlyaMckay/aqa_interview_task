Feature: Click the first result

	Scenario: User should click the first result in the list
		Given The results list
		When User clicks the first search result
		Then The city weather page header contains the city name from the search