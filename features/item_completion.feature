Feature:As a user, I want to use the TodoMVC app so that I can efficiently manage and organize my tasks

  # Scenario 3: Marking an item as complete
  Scenario: Item completion changes the list
    Given a Todo list with items "Work on assignment" & "Review assignment draft"
    When the first item is marked as complete
    Then only the second item is listed as active
    And the list summary is "1 item left!"

Scenario: Completed items should not be visible in active filter
  When the filter is set to "Active"
  Then only the second item is listed as active
  And the list summary is "1 item left!"
  And the route is "/active"


  Scenario: Uncompleted items should not be visible in the completed filter
    When the filter is set to "Completed"
    Then only the first item is listed
    And the list summary is "1 item left!"
    And the route is "/completed"

  # Scenario 5: All items completed in active filter
  Scenario: All completed items should not be visible in active filter
    When the filter is set to "Active"
    When the first item is marked as complete
    Then nothing is listed
    And the list summary is "0 items left!"
    And the route is "/active"

   Scenario: Filtering completed items
     When the filter is set to "All"
     And the first item is marked as complete
     Then "Clear completed" is clicked
     Then the list summary is "1 item left!"


