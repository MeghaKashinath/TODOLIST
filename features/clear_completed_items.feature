Feature: Clearing Completed Todos

  Scenario: Mark one or more Todos as complete and click Clear completed
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When the first item is marked as complete
    When the second item is marked as complete
    Then "Clear completed" is clicked
    And the remaining Todo item "Learn a new skill" should stay in the list
    When the filter is set to "All"
    And I click on the select all toggle button
    Then "Clear completed" is clicked



Scenario: Validate that active Todos remain unaffected when clearing completed Todos
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When the first item is marked as complete
    Then "Clear completed" is clicked
    Then no active Todo items should be removed or affected by clicking "Clear completed"
    When the filter is set to "All"
    And I click on the select all toggle button
    Then "Clear completed" is clicked

