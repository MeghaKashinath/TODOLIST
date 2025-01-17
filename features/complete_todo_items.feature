Feature: Marking Todos as Complete
  As a user of the Todo application,
  I want to mark Todos as complete
  So that I can keep track of tasks I have finished.

Scenario: Mark a single Todo as complete
    Given the Todo list contains the item "Buy groceries"
    When the first item is marked as complete
    Then the list summary is "0 items left!"
    And "Clear completed" is clicked


Scenario: Mark multiple Todos as complete
    When I add Todos for "Buy milk" & "Call a friend" & "Learn a new skill"
    And the first item is marked as complete
    And the second item is marked as complete
    Then the list summary is "1 item left!"
    When I click on the select all toggle button
    Then "Clear completed" is clicked


Scenario: Validate that completed Todos are displayed correctly
    Given a Todo list with items "Work on assignment" & "Review assignment draft"
    When the first item is marked as complete
    And the filter is set to "Completed"
    Then only the first item is listed
    When the filter is set to "All"
    And I click on the select all toggle button
    Then "Clear completed" is clicked



