Feature: Filtering Todos


  Scenario: Set the filter to All and verify that all Todos are visible
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When the filter is set to "All"
    Then all the Todo items should be visible in the list
    When I click on the select all toggle button
    Then "Clear completed" is clicked


  Scenario: Set the filter to Active and verify that only active Todos are visible
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When the first item is marked as complete
    And the filter is set to "Active"
    Then only the active Todo items should be visible in the list
    And the route is "/active"
    When I click on the select all toggle button
    Then "Clear completed" is clicked


  Scenario: Set the filter to Completed and verify that only completed Todos are visible
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When the first item is marked as complete
    And the filter is set to "Completed"
    Then only the completed Todo items should be visible in the list
    And the route is "/completed"
    When the filter is set to "All"
    And I click on the select all toggle button
    Then "Clear completed" is clicked
