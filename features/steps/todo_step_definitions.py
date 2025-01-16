from behave import *
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time


# Step Definitions for the Todo List

# Given Steps

@given('the Todo list is empty')
def given_empty_list(context):
    """Ensure the Todo list is empty."""
    todo_list = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_list) == 0, "The Todo list is not empty."


@given('a Todo list with items "{item1}" & "{item2}"')
def given_todo_list_with_items(context, item1, item2):
    """Create a Todo list with two items."""
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')

    # Add item1 to the list
    input_field.send_keys(item1)
    input_field.send_keys(Keys.RETURN)

    # Add item2 to the list
    input_field.send_keys(item2)
    input_field.send_keys(Keys.RETURN)

    # Verify both items are added
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    assert item1 in item_labels, f"Item '{item1}' was not added."
    assert item2 in item_labels, f"Item '{item2}' was not added."


# When Steps

@when('I add a Todo item labeled "{todo_item}"')
def add_todo_item(context, todo_item):
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(todo_item)
    input_field.send_keys(Keys.RETURN)



@when('I add Todos for "{todo_item1}" & "{todo_item2}" & "{todo_item3}"')
def add_multiple_todos(context, todo_item1, todo_item2, todo_item3):
    """Add multiple Todo items."""
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')

    # Add first item
    input_field.send_keys(todo_item1)
    input_field.send_keys(Keys.RETURN)
    time.sleep(1)

    # Add second item
    input_field.send_keys(todo_item2)
    input_field.send_keys(Keys.RETURN)
    time.sleep(1)

    # Add third item
    input_field.send_keys(todo_item3)
    input_field.send_keys(Keys.RETURN)
    time.sleep(1)


@when('I click on the cross symbol next to the Todo item')
def click_cross_symbol(context):
    """Click the cross symbol to delete a Todo item."""
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="todo-list"]/li'))
    )

    # Find the last added Todo item
    last_todo_item = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[last()]'))
    )

    # Hover to reveal the cross button
    actions = ActionChains(context.driver)
    actions.move_to_element(last_todo_item).perform()

    # Click the cross button
    cross_button = last_todo_item.find_element(By.XPATH, './/button[contains(@class, "destroy")]')
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(cross_button))
    cross_button.click()


@when('the first item is marked as complete')
def mark_first_item_complete(context):
    """Mark the first Todo item as complete."""
    first_item_checkbox = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[1]//input[@type="checkbox"]'))
    )
    first_item_checkbox.click()
    time.sleep(5)


@when('the filter is set to "Active"')
def set_filter_to_active(context):
    """Set the filter to show only active items."""
    active_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="Active"]'))
    )
    active_filter.click()
    time.sleep(3)


@when('the filter is set to "All"')
def set_filter_to_all(context):
    """Set the filter to show all Todo items."""
    all_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="All"]'))
    )
    all_filter.click()
    time.sleep(3)


@when('the filter is set to "Completed"')
def set_filter_to_completed(context):
    """Set the filter to show only completed items."""
    completed_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="Completed"]'))
    )
    completed_filter.click()
    time.sleep(2)


@when('all items are marked as complete')
def mark_all_items_complete(context):
    """Mark all Todo items as complete."""
    checkboxes = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li//input[@type="checkbox"]')
    for checkbox in checkboxes:
        checkbox.click()



@when('I click on the select all toggle button')
def click_select_all_toggle(context):
    select_all_checkbox = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@class="toggle-all"]'))
    )
    ActionChains(context.driver).move_to_element(select_all_checkbox).click().perform()
time.sleep(1)

#
# @when('the item is selected for edit')
# def select_item_for_edit(context):
#     """Select the Todo item for editing."""
#     # Find the label text for the Todo item
#     todo_item = context.driver.find_element(By.XPATH, "//label[text()='Clean the house']")
#
#     # Double-click the item to enter edit mode
#     actions = ActionChains(context.driver)
#     actions.double_click(todo_item).perform()
#     time.sleep(10)
#     todo_item = context.driver.find_element(By.XPATH, "//*[contains(text(),'Clean the house')]")
#     todo_item.clear()
#     todo_item.send_keys("Meditate")
#
#     # Press Enter to confirm the change
#     todo_item.send_keys(Keys.RETURN)


@when('the item is selected for edit')
def select_item_for_edit(context):
    """Select the Todo item for editing and concatenate a new value to the existing item."""
    try:
        # Find the label text for the Todo item
        todo_item_label = context.driver.find_element(By.XPATH, "//label[text()='Clean the house']")
        print("Todo label found, proceeding to double-click.")

        # Perform double-click to enter edit mode
        actions = ActionChains(context.driver)
        actions.double_click(todo_item_label).perform()

        # Find the input field directly (adjust the XPath as necessary)
        input_field = context.driver.find_element(By.XPATH,
                                                  "//input[@type='text']")  # Adjusted XPath based on type='text'

        # Get the current value from the input field
        current_value = input_field.get_attribute("value")  # This is the current Todo text

        # Define the new value to concatenate
        new_value = " and organize it"  # This is the text you want to add

        # Concatenate the current value with the new value
        concatenated_value = current_value + new_value  # Now the value is a combination of both

        # Clear the input field and send the concatenated value
        input_field.clear()  # Clear the existing value
        input_field.send_keys(concatenated_value)  # Enter the concatenated value back into the input field

        # Optionally, you can press ENTER to save the item after editing
        input_field.send_keys(Keys.RETURN)  # Press Enter to confirm the change

        # Wait briefly to ensure the new value is set
        time.sleep(1)
        print(f"Todo item updated: {concatenated_value}")

    except Exception as e:
        print(f"Error encountered during the test: {e}")
# Then Steps

@then('the list displays the item "Buy Grocery"')
def check_item_displayed(context):
    """Verify that the "Buy Grocery" item is displayed in the Todo list."""
    time.sleep(5)
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    assert "Buy Grocery" in item_labels, "'Buy Grocery' was not added to the list."


@then('only those items are listed')
def check_multiple_items(context):
    """Verify that only the specified items are listed."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]

    assert len(item_labels) == 3, f"Expected 3 items, but found {len(item_labels)}"
    assert "Buy milk" in item_labels
    assert "Call a friend" in item_labels
    assert "Learn a new skill" in item_labels


@then('the summary shows "{summary_text}"')
def check_summary(context, summary_text):
    """Verify the summary text in the Todo list footer."""
    summary = context.driver.find_element(By.XPATH, '//footer//span[@class="todo-count"]')
    assert summary.text == summary_text, f"Expected '{summary_text}', but got {summary.text}"


@then('the filter is set to "All" with no filters "Completed" or "Active" applied')
def check_filter(context):
    """Verify that the "All" filter is applied."""
    filter_all = context.driver.find_element(By.XPATH, '//ul[@class="filters"]/li/a[@class="selected"]')
    assert filter_all.text == "All", "The filter is not set to 'All'"



@then('only the second item is listed as active')
def verify_only_second_item_active(context):
    """Verify that only the second item is listed as active."""
    active_items = context.driver.find_elements(By.XPATH,
                                                '//ul[@class="todo-list"]/li[not(contains(@class, "completed"))]')
    active_item_labels = [item.text for item in active_items]

    assert len(active_item_labels) == 1, f"Expected 1 active item, but found {len(active_item_labels)}"
    assert "Review assignment draft" in active_item_labels, f"'Review assignment draft' is not listed as active."

@then('the route is "{route}"')
def verify_route(context, route):
    # Verify the current URL ends with the expected route
    current_url = context.driver.current_url
    assert current_url.endswith(route), f"Expected route '{route}', but got '{current_url}'"


@then('nothing is listed')
def verify_nothing_listed(context):
    """Verify that no active Todo items are listed."""
    active_items = context.driver.find_elements(By.XPATH,
                                                '//ul[@class="todo-list"]/li[not(contains(@class, "completed"))]')
    assert len(active_items) == 0, "Expected no active items, but found some."


@then('only the first item is listed')
def verify_only_first_item_listed(context):
    """Verify that only the first item (completed) is listed."""
    completed_items = context.driver.find_elements(By.XPATH,
                                                   '//ul[@class="todo-list"]/li[contains(@class, "completed")]')
    completed_item_labels = [item.text for item in completed_items]

    assert len(completed_item_labels) == 1, f"Expected 1 completed item, but found {len(completed_item_labels)}"
    assert "Work on assignment" in completed_item_labels, f"'Work on assignment' is not listed as completed."


@then('"Clear completed" is clicked')
def step_impl(context):
    # Locate the "Clear completed" button
    clear_completed_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Clear completed')]"))
    )
    assert clear_completed_button.is_displayed(), '"Clear completed" button is not displayed'

    # Click the "Clear completed" button
    clear_completed_button.click()

    # Ensure completed items are cleared from the DOM
    completed_items = context.driver.find_elements(By.XPATH, "//li[contains(@class, 'completed')]")
    assert len(completed_items) == 0, "Completed items are still present after clicking 'Clear completed'"
    time.sleep(3)

@then('the list is empty')
def verify_list_is_empty(context):
    """Verify that the Todo list is empty after clearing all items."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_items) == 0, "The Todo list is not empty."

@then('the list summary is "{summary_text}"')
def verify_list_summary(context, summary_text):
    # Verify the summary text in the footer
    summary_element = context.driver.find_element(By.XPATH, '//footer//span[@class="todo-count"]')
    assert summary_element.text == summary_text, f"Expected summary '{summary_text}', but got '{summary_element.text}'"
    time.sleep(2)


# @then('only the revised item is listed')
# def verify_revised_item_listed(context):
#     # Check that the revised item "Meditate" is in the list and that it is the only item
#     todo_items = context.driver.find_elements(By.XPATH, "//ul[@class='todo-list']/li")
#     assert len(todo_items) == 1, f"Expected 1 item, but found {len(todo_items)}"
#     assert "Meditate" in todo_items[0].text, f"Expected 'Meditate', but found {todo_items[0].text}"



# @when('the Todo is changed to "{new_value}"')
# def step_impl(context, new_value):
#     # Locate the edit input field that appears when the label is in edit mode
#     # edit_input = context.driver.find_element(By.XPATH, "//input[@class='input-container']")
#     #
#     # # Clear the current value and enter the new value
#     # edit_input.clear()
#     edit_input.send_keys(new_value)
#
#     # Press Enter to confirm the change
#     edit_input.send_keys(Keys.RETURN)


@then('only the revised item is listed')
def step_impl(context):
    # Locate the updated label to verify the value
    updated_label = context.driver.find_element(By.XPATH, "//label[@data-testid='todo-item-label' and text()='Meditate']")
    assert updated_label.text == "Meditate", f"Expected 'Meditate', but found '{updated_label.text}'"

    #####################################

@then('the tasks are labeled')
def step_impl(context):
    """Verify that the correct tasks are labeled on the Todo list."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    for row in context.table:
        assert row[0] in item_labels, f"Item '{row[0]}' was not added correctly."
        #assert row['Task'] in item_labels, f"Item '{row['Task']}' was not added correctly."

@when('I leave the Todo input box empty')
def leave_todo_input_empty(context):
    """Leave the Todo input box empty."""
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.clear()


@when('I press the Enter key')
def press_enter_key(context):
    """Simulate pressing the Enter key."""
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(Keys.RETURN)

# Then Steps
@then('no new task is added to the Todo list')
def no_task_added_to_list(context):
    """Verify that no new task is added to the Todo list."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_items) == 0, "A task was unexpectedly added to the list."

# @then('the Todo list remains unchanged')
# def todo_list_remains_unchanged(context):
#     """Verify that the Todo list remains unchanged."""
#     initial_todo_count = len(context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li'))
#     todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
#     assert len(todo_items) == initial_todo_count, "The Todo list was unexpectedly changed."



@then('the Todo list remains unchanged.')
def step_impl(context):
    """Ensure that the Todo list remains unchanged after attempting to add a blank Todo item."""
    # Get the initial number of items in the Todo list
    initial_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    initial_count = len(initial_items)

    # Perform the action to add a blank Todo (leave input box empty and press Enter)
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys("")  # Leave the input empty
    input_field.send_keys(Keys.RETURN)

    # Wait for the UI to update and get the number of items again
    time.sleep(1)  # Adjust the sleep time based on your application's responsiveness
    updated_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    updated_count = len(updated_items)

    # Assert that the number of items has not changed
    assert initial_count == updated_count, f"Expected Todo list to remain unchanged, but the number of items changed from {initial_count} to {updated_count}."



