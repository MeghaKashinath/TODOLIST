Feature: Deleting Todos
  As a user of the Todo application,
  I want to be able to delete individual Todo items from the list,
  So that I can remove tasks I no longer need to track.


Scenario: Verify that a user can delete a single Todo item from the list by clicking the delete (X) button next to it
   Given the Todo list contains the item "Buy groceries"
   When I hover click the delete button (X) next to the Todo item
   Then nothing is listed

Scenario: Delete multiple Todos
   When I add Todos for "Buy milk" & "Call a friend" & "Learn a new skill"
   And I hover click the delete button (X) next to the Todo item
   And I hover click the delete button (X) next to the Todo item
   Then the summary shows "1 item left!"
   When I click on the select all toggle button
   Then "Clear completed" is clicked





