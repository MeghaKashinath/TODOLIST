from time import sleep

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('a Todo list with items "{item1}" & "{item2}"')
def given_todo_list_with_items(context, item1, item2):
    # Add the first item
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(item1)
    input_field.send_keys(Keys.RETURN)

    # Add the second item
    input_field.send_keys(item2)
    input_field.send_keys(Keys.RETURN)

    # Verify the items are added
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    assert item1 in item_labels, f"Item '{item1}' was not added."
    assert item2 in item_labels, f"Item '{item2}' was not added."


@when('the first item is marked as complete')
def mark_first_item_complete(context):
    # Find the first item's checkbox and mark it as complete
    first_item_checkbox = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[1]//input[@type="checkbox"]'))
    )
    first_item_checkbox.click()

    time.sleep(5)


@then('only the second item is listed as active')
def verify_only_second_item_active(context):
    # Get the list of active items (those without the "completed" class)
    active_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li[not(contains(@class, "completed"))]')
    active_item_labels = [item.text for item in active_items]

    # Verify that only one item is active, and it's the second item
    assert len(active_item_labels) == 1, f"Expected 1 active item, but found {len(active_item_labels)}"
    assert "Review assignment draft" in active_item_labels, f"'Review assignment draft' is not listed as active."


@then('the list summary is "{summary_text}"')
def verify_list_summary(context, summary_text):
    # Verify the summary text in the footer
    summary_element = context.driver.find_element(By.XPATH, '//footer//span[@class="todo-count"]')
    assert summary_element.text == summary_text, f"Expected summary '{summary_text}', but got '{summary_element.text}'"
    time.sleep(5)

@when('the filter is set to "Active"')
def set_filter_to_active(context):
    # Click the "Active" filter link
    active_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="Active"]'))
    )
    active_filter.click()
    time.sleep(3)  # Give it a moment to update the UI

@when('the filter is set to "All"')
def set_filter_to_active(context):
    # Click the "Active" filter link
    active_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="All"]'))
    )
    active_filter.click()
    time.sleep(3)


@then('only the second item is listed')
def verify_only_second_item_listed(context):
    # Verify the list displays only the second item (the active one)
    active_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    active_item_labels = [item.text for item in active_items]

    assert len(active_item_labels) == 1, f"Expected 1 active item, but found {len(active_item_labels)}"
    assert "Review assignment draft" in active_item_labels, f"'Review assignment draft' is not listed as active."


@then('the route is "{route}"')
def verify_route(context, route):
    # Verify the current URL ends with the expected route
    current_url = context.driver.current_url
    assert current_url.endswith(route), f"Expected route '{route}', but got '{current_url}'"


@when('all items are marked as complete')
def mark_all_items_complete(context):
    # Find all checkboxes and mark them as complete
    checkboxes = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li//input[@type="checkbox"]')
    for checkbox in checkboxes:
        checkbox.click()


@then('nothing is listed')
def verify_nothing_listed(context):
    # Verify that no active items are displayed
    active_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li[not(contains(@class, "completed"))]')
    assert len(active_items) == 0, "Expected no active items, but found some."
    time.sleep(5)


@when('the filter is set to "Completed"')
def set_filter_to_completed(context):
    # Click the "Completed" filter link
    completed_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="filters"]/li/a[text()="Completed"]'))
    )
    completed_filter.click()
    time.sleep(2)  # Give it a moment to update the UI


@then('only the first item is listed')
def verify_only_first_item_listed(context):
    # Get the list of completed items (those with the "completed" class)
    completed_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li[contains(@class, "completed")]')
    completed_item_labels = [item.text for item in completed_items]

    # Verify that only the first item is listed as completed
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


