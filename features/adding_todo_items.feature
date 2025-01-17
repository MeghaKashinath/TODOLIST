Feature: Adding Todos
  As a user of the Todo application,
  I want to add tasks to my list
  So that I can keep track of and manage my daily activities effectively.


Scenario: Add a single Todo item when the Todo list is initially empty
    Given the Todo list is empty
    When I add a Todo item labeled "Buy Grocery"
    Then the list displays the item "Buy Grocery"
    And the summary shows "1 item left!"
    And the filter is set to "All" with no filters "Completed" or "Active" applied
    When I click on the select all toggle button
    Then "Clear completed" is clicked

Scenario: Add multiple Todo items to the list and verify that all items are displayed in the correct order.
    Given the Todo list is empty
    When I add Todos for "Buy milk" & "Call a friend" & "Learn a new skill"
    Then only those items are listed
    And the summary shows "3 items left!"
    And the filter is set to "All" with no filters "Completed" or "Active" applied
    And the tasks are labeled:
      | Buy milk  |
      | Call a friend |
      | Learn a new skill  |
    When I click on the select all toggle button
    Then "Clear completed" is clicked


Scenario: Ensure that adding a blank Todo is not allowed
    Given the Todo list is empty
    When I press the Enter key
    Then no new task is added to the Todo list
    And the Todo list remains unchanged.





