Feature: Toggle All Todos in Todo List and Displaying the Correct Summary

  Scenario: Marking all Todos as complete using the toggle button
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When I click on the select all toggle button
    Then the list summary is "0 items left!"
    And "Clear completed" is clicked


  Scenario: Unmarking all Todos as active using the toggle button
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When I click on the select all toggle button
    And I click on the select all toggle button
    Then the list summary is "3 items left!"
    When I click on the select all toggle button
    Then "Clear completed" is clicked

Scenario: Add Todos and verify the summary updates
    Given the Todo list is empty
    When I add a Todo item labeled "Buy Grocery"
    Then the summary shows "1 item left!"

Scenario: Adding multiple Todos and verifying the summary
    Given the Todo list contains the items "Buy groceries" & "Call a friend" & "Learn a new skill"
    When I add a Todo item labeled "Buy Milk"
    Then the summary shows "5 items left!"
    When I click on the select all toggle button
    Then "Clear completed" is clicked