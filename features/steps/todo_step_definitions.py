import logging

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

from features.environment import capture_screenshot


# Step Definitions for the Todo List

# Given Steps

@given('the Todo list is empty')
def given_empty_list(context):
    """Ensure the Todo list is empty."""
    todo_list = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_list) == 0, "The Todo list is not empty."
    capture_screenshot(context.driver, 'the Todo list is empty')



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
    capture_screenshot(context.driver, 'a Todo list with multiple items')



@given('the Todo list contains the item "{todo_item}"')
def add_todo_item(context, todo_item):
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(todo_item)
    input_field.send_keys(Keys.RETURN)
    time.sleep(1)
    capture_screenshot(context.driver, 'the Todo list contains the single item')


@given('the Todo list contains the items "{todo_item1}" & "{todo_item2}" & "{todo_item3}"')
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
    capture_screenshot(context.driver, 'the Todo list contains 3 items')


@when('I add a Todo item labeled "{todo_item}"')
def add_todo_item(context, todo_item):
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(todo_item)
    input_field.send_keys(Keys.RETURN)
    time.sleep(1)
    capture_screenshot(context.driver, 'add a Todo item to the list')


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
    capture_screenshot(context.driver, 'add multiple Todo items to the list')

#Hover over and click the delete button (X)
@when('I hover click the delete button (X) next to the Todo item')
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
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(cross_button))
    cross_button.click()
    time.sleep(1)
    capture_screenshot(context.driver, 'click the delete button (X) next to the Todo item')


@when('the first item is marked as complete')
def mark_first_item_complete(context):
    """Mark the first Todo item as complete."""
    first_item_checkbox = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[1]//input[@type="checkbox"]'))
    )
    first_item_checkbox.click()
    time.sleep(1)
    capture_screenshot(context.driver, 'the first item is marked as complete')


@when('the second item is marked as complete')
def mark_second_item_complete(context):
    """Mark the first Todo item as complete."""
    second_item_checkbox = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[2]//input[@type="checkbox"]'))
    )
    second_item_checkbox.click()
    time.sleep(1)
    capture_screenshot(context.driver, 'the second item is marked as complete')


@when('the filter is set to "Active"')
def set_filter_to_active(context):
    """Set the filter to show only active items."""
    active_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="Active"]'))
    )
    active_filter.click()
    time.sleep(3)
    capture_screenshot(context.driver, 'the filter is set to "Active"')


@when('the filter is set to "All"')
def set_filter_to_all(context):
    """Set the filter to show all Todo items."""
    all_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="All"]'))
    )
    all_filter.click()
    time.sleep(3)
    capture_screenshot(context.driver, 'the filter is set to "All"')


@when('the filter is set to "Completed"')
def set_filter_to_completed(context):
    """Set the filter to show only completed items."""
    completed_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="Completed"]'))
    )
    completed_filter.click()
    time.sleep(2)
    capture_screenshot(context.driver, 'the filter is set to "Completed"')

@when('all items are marked as complete')
def mark_all_items_complete(context):
    """Mark all Todo items as complete."""
    checkboxes = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li//input[@type="checkbox"]')
    for checkbox in checkboxes:
        checkbox.click()
    capture_screenshot(context.driver, 'all items are marked as complete')

@when('I click on the select all toggle button')
def click_select_all_toggle(context):
    select_all_checkbox = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@class="toggle-all"]'))
    )
    ActionChains(context.driver).move_to_element(select_all_checkbox).click().perform()
    time.sleep(1)
    capture_screenshot(context.driver, 'click on the select all toggle button')


@when('I press the Enter key')
def press_enter_key(context):
    """Simulate pressing the Enter key."""
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(Keys.RETURN)
    capture_screenshot(context.driver, 'press the Enter key')

@when('I check the checkbox next to the Todos labeled {items}')
def step_when_check_multiple_checkboxes(context, items):
    # Split the items by 'and' and strip whitespace
    item_list = [item.strip() for item in items.split(' and ')]

    # Loop through each item and check its checkbox
    for item in item_list:
        checkbox = context.browser.find_element(
            By.XPATH, f'//ul[@class="todo-list"]/li[.//label[text()="{item}"]]//input[@class="toggle"]'
        )
        checkbox.click()
    capture_screenshot(context.driver, 'check the checkbox next to the Todo item')

@then('the list displays the item "{item_label}"')
def check_item_displayed(context, item_label):
    """Verify that a given item is displayed in the Todo list."""
    time.sleep(2)  # You can adjust or remove this if not needed
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    assert item_label in item_labels, f"'{item_label}' was not added to the list."
    capture_screenshot(context.driver, 'the list displays a item')

@then('only those items are listed')
def check_multiple_items(context):
    """Verify that only the specified items are listed."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]

    assert len(item_labels) == 3, f"Expected 3 items, but found {len(item_labels)}"
    assert "Buy milk" in item_labels
    assert "Call a friend" in item_labels
    assert "Learn a new skill" in item_labels
    capture_screenshot(context.driver, 'the list displays 3 items')


@then('the summary shows "{summary_text}"')
def check_summary(context, summary_text):
    """Verify the summary text in the Todo list footer."""
    summary = context.driver.find_element(By.XPATH, '//footer//span[@class="todo-count"]')
    assert summary.text == summary_text, f"Expected '{summary_text}', but got {summary.text}"
    capture_screenshot(context.driver, 'summary text')


@then('the filter is set to "All" with no filters "Completed" or "Active" applied')
def check_filter(context):
    """Verify that the "All" filter is applied."""
    filter_all = context.driver.find_element(By.XPATH, '//ul[@class="filters"]/li/a[@class="selected"]')
    assert filter_all.text == "All", "The filter is not set to 'All'"
    capture_screenshot(context.driver, 'the filter is set to "All" with no filters "Completed" or "Active" applied')

@then('only the second item is listed as active')
def verify_only_second_item_active(context):
    """Verify that only the second item is listed as active."""
    active_items = context.driver.find_elements(By.XPATH,
                                                '//ul[@class="todo-list"]/li[not(contains(@class, "completed"))]')
    active_item_labels = [item.text for item in active_items]

    assert len(active_item_labels) == 1, f"Expected 1 active item, but found {len(active_item_labels)}"
    assert "Review assignment draft" in active_item_labels, f"'Review assignment draft' is not listed as active."
    capture_screenshot(context.driver, 'only the second item is listed as active')

@then('the route is "{route}"')
def verify_route(context, route):
    # Verify the current URL ends with the expected route
    current_url = context.driver.current_url
    assert current_url.endswith(route), f"Expected route '{route}', but got '{current_url}'"
    capture_screenshot(context.driver, 'current route url')

@then('nothing is listed')
def verify_nothing_listed(context):
    """Verify that no active Todo items are listed."""
    active_items = context.driver.find_elements(By.XPATH,
                                                '//ul[@class="todo-list"]/li[not(contains(@class, "completed"))]')
    assert len(active_items) == 0, "Expected no active items, but found some."
    capture_screenshot(context.driver, 'nothing is listed')

@then('only the first item is listed')
def verify_only_first_item_listed(context):
    """Verify that only the first item (completed) is listed."""
    completed_items = context.driver.find_elements(By.XPATH,
                                                   '//ul[@class="todo-list"]/li[contains(@class, "completed")]')
    completed_item_labels = [item.text for item in completed_items]

    assert len(completed_item_labels) == 1, f"Expected 1 completed item, but found {len(completed_item_labels)}"
    assert "Work on assignment" in completed_item_labels, f"'Work on assignment' is not listed as completed."
    capture_screenshot(context.driver, 'only the first item is listed')

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
    capture_screenshot(context.driver, '"Clear completed" is clicked')

@then('the list is empty')
def verify_list_is_empty(context):
    """Verify that the Todo list is empty after clearing all items."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_items) == 0, "The Todo list is not empty."
    capture_screenshot(context.driver, 'the list is empty')

@then('the list summary is "{summary_text}"')
def verify_list_summary(context, summary_text):
    # Verify the summary text in the footer
    summary_element = context.driver.find_element(By.XPATH, '//footer//span[@class="todo-count"]')
    assert summary_element.text == summary_text, f"Expected summary '{summary_text}', but got '{summary_element.text}'"
    time.sleep(2)
    capture_screenshot(context.driver, 'the list summary verification')

@then('only the revised item is listed')
def step_impl(context):
    # Locate the updated label to verify the value
    updated_label = context.driver.find_element(By.XPATH, "//label[@data-testid='todo-item-label' and text()='Meditate']")
    assert updated_label.text == "Meditate", f"Expected 'Meditate', but found '{updated_label.text}'"
    capture_screenshot(context.driver, 'only the revised item is listed')

@then('the tasks are labeled')
def step_impl(context):
    """Verify that the correct tasks are labeled on the Todo list."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    for row in context.table:
        assert row[0] in item_labels, f"Item '{row[0]}' was not added correctly."
    capture_screenshot(context.driver, 'the tasks are labeled')

# Then Steps
@then('no new task is added to the Todo list')
def no_task_added_to_list(context):
    """Verify that no new task is added to the Todo list."""
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_items) == 0, "A task was unexpectedly added to the list."
    capture_screenshot(context.driver, 'no new task is added to the Todo list')

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
    capture_screenshot(context.driver, 'the Todo list remains unchanged')

@then('all the Todo items should be visible in the list')
def step_then_all_items_visible(context):
    todo_items = context.driver.find_elements(By.XPATH, "//ul[@class='todo-list']/li")
    assert len(todo_items) > 0, "No Todo items are visible."
    capture_screenshot(context.driver, 'all the Todo items should be visible in the list')

@then('only the active Todo items should be visible in the list')
def step_then_active_items_visible(context):
    todo_items = context.driver.find_elements(By.XPATH, "//ul[@class='todo-list']/li")
    active_items = [item for item in todo_items if "completed" not in item.get_attribute("class")]
    assert len(active_items) > 0, "No active items found"
    capture_screenshot(context.driver, 'only the active Todo items should be visible in the list')

@then('only the completed Todo items should be visible in the list')
def verify_completed_todos_visible(context):
    """Verify that only completed Todo items are visible in the list."""
    # Find all visible Todo items
    visible_todos = context.driver.find_elements(By.XPATH, "//ul[@class='todo-list']/li")

    # Check that each visible Todo item has the 'completed' class
    for todo_item in visible_todos:
        assert "completed" in todo_item.get_attribute("class"), "Found an incomplete Todo item."

    logging.info("Only completed Todo items are visible.")
    capture_screenshot(context.driver, 'only the active Todo items should be visible in the list')

@then('the remaining Todo item "Learn a new skill" should stay in the list')
def step_impl(context):
    """Ensure that 'Learn a new skill' stays in the Todo list after removal of others."""

    # Wait for the Todo list to update
    time.sleep(2)

    # Get all Todo items
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]

    # Ensure that "Learn a new skill" remains in the list
    assert "Learn a new skill" in item_labels, "'Learn a new skill' was removed."
    capture_screenshot(context.driver, 'the remaining Todo item "Learn a new skill" should stay in the list')

@then('no active Todo items should be removed or affected by clicking "Clear completed"')
def step_impl(context):
    """Ensure no active Todo items are removed or affected when clicking 'Clear completed'."""

    # Store the initial list of active Todo items
    initial_active_items = [item.text for item in
                            context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li[@class="active"]')]

    # Click the "Clear completed" button
    clear_completed_button = context.driver.find_element(By.XPATH, '//button[@class="clear-completed"]')
    clear_completed_button.click()

    # Wait for the list to update
    time.sleep(2)

    # Get the updated list of active Todo items
    updated_active_items = [item.text for item in
                            context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li[@class="active"]')]

    # Ensure that no active items were removed or affected
    assert initial_active_items == updated_active_items, "Active Todo items were removed or affected by clicking 'Clear completed'."
    capture_screenshot(context.driver, 'no active Todo items should be removed or affected by clicking "Clear completed"')
