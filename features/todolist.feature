Feature:As a user, I want to use the TodoMVC app so that I can efficiently manage and organize my tasks
#  Scenario: Adding an item to an empty Todo list
#    Given the Todo list is empty
#    When I add a Todo item labeled "Buy Grocery"
#    Then the list displays the item "Buy Grocery"
#    And the summary shows "1 item left!"
#    And the filter is set to "All" with no filters "Completed" or "Active" applied
#    When I click on the cross symbol next to the Todo item

    # Scenario: Adding three items to an empty list
  Scenario: Empty list can have three items added
    Given the Todo list is empty
    When I add Todos for "Buy milk" & "Call a friend" & "Learn a new skill"
    Then only those items are listed
    And the summary shows "3 items left!"
    And the filter is set to "All" with no filters "Completed" or "Active" applied



  Scenario: Clear all items from a populated Todo list
    When I click on the select all toggle button
    Then the list summary is "0 items left!"
    And "Clear completed" is clicked
    Then the list is empty




