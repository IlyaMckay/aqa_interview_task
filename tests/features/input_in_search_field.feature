Feature: Input data in the search field

    Scenario Outline: User should input data in the search field
        Given The website's main page is open
        When User inputs the <city_name>
        Then User sees the results list
        Examples: 
        | city_name |
        | New-York  |
        | London    |