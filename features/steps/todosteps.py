from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
import time

from selenium.webdriver.support.wait import WebDriverWait


@when('I click on the cross symbol next to the Todo item')
def click_cross_symbol(context):
    # Wait for the Todo list to be updated (ensure the list has at least one item)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="todo-list"]/li'))
    )

    # Find the last added Todo item (the one we just added)
    last_todo_item = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[last()]'))
    )

    # Hover over the entire Todo item to make the delete button visible
    actions = ActionChains(context.driver)
    actions.move_to_element(last_todo_item).perform()  # Hover over the todo item to reveal the cross button

    # Now that the cross button should be visible, find the button
    cross_button = last_todo_item.find_element(By.XPATH, './/button[contains(@class, "destroy")]')

    # Wait until the button is clickable
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(cross_button)
    )

    # Click the cross button to delete the item
    cross_button.click()

@given('the Todo list is empty')
def given_empty_list(context):
    # Ensure the input field is available to confirm the page has loaded
    todo_list = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    assert len(todo_list) == 0, "The Todo list is not empty."


@when('I add a Todo item labeled "Buy Grocery"')
def add_todo_item(context):
    # Find the input field and add a new Todo item
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys("Buy Grocery")
    input_field.send_keys(Keys.RETURN)  # Press ENTER to add the item


@when('I add Todos for "{todo_item1}" & "{todo_item2}" & "{todo_item3}"')
def add_multiple_todos(context, todo_item1, todo_item2, todo_item3):
    # Find the input field and add the first Todo item
    input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
    input_field.send_keys(todo_item1)
    input_field.send_keys(Keys.RETURN)  # Press ENTER to add the item
    time.sleep(1)  # Adding some delay to ensure the items are added in order

    # Add the second Todo item
    input_field.send_keys(todo_item2)
    input_field.send_keys(Keys.RETURN)  # Press ENTER to add the item
    time.sleep(1)

    # Add the third Todo item
    input_field.send_keys(todo_item3)
    input_field.send_keys(Keys.RETURN)  # Press ENTER to add the item
    time.sleep(1)


@then('the list displays the item "Buy Grocery"')
def check_item_displayed(context):
    # Wait a bit for the item to be added to the list
    time.sleep(5)
    # Use XPath to locate all items in the Todo list
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]
    # Check if "Buy Grocery" is present in the list
    assert "Buy Grocery" in item_labels, "'Buy Grocery' was not added to the list."


@then('only those items are listed')
def check_multiple_items(context):
    # Get all todo items and verify if the correct number of items are listed
    todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
    item_labels = [item.text for item in todo_items]

    assert len(item_labels) == 3, f"Expected 3 items, but found {len(item_labels)}"
    assert "Buy milk" in item_labels
    assert "Call a friend" in item_labels
    assert "Learn a new skill" in item_labels


@then('the summary shows "{summary_text}"')
def check_summary(context, summary_text):
    # Find the summary element and verify the text using XPath
    summary = context.driver.find_element(By.XPATH, '//footer//span[@class="todo-count"]')
    assert summary.text == summary_text, f"Expected '{summary_text}', but got {summary.text}"


@then('the filter is set to "All" with no filters "Completed" or "Active" applied')
def check_filter(context):
    # Use XPath to verify that the "All" filter is selected
    filter_all = context.driver.find_element(By.XPATH, '//ul[@class="filters"]/li/a[@class="selected"]')
    assert filter_all.text == "All", "The filter is not set to 'All'"





