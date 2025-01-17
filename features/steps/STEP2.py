from behave import *
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time


# @when('the second item is marked as complete')
# def mark_second_item_complete(context):
#     """Mark the first Todo item as complete."""
#     second_item_checkbox = WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//ul[@class="todo-list"]/li[2]//input[@type="checkbox"]'))
#     )
#     second_item_checkbox.click()
#     time.sleep(1)


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


# @then('the list displays the item "Buy Grocery"')
# def check_item_displayed(context):
#     """Verify that the "Buy Grocery" item is displayed in the Todo list."""
#     time.sleep(5)
#     todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
#     item_labels = [item.text for item in todo_items]
#     assert "Buy Grocery" in item_labels, "'Buy Grocery' was not added to the list."


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


        #assert row['Task'] in item_labels, f"Item '{row['Task']}' was not added correctly."

# @when('I leave the Todo input box empty')
# def leave_todo_input_empty(context):
#     """Leave the Todo input box empty."""
#     input_field = context.driver.find_element(By.XPATH, '//input[@class="new-todo"]')
#     input_field.clear()



# @then('the Todo list remains unchanged')
# def todo_list_remains_unchanged(context):
#     """Verify that the Todo list remains unchanged."""
#     initial_todo_count = len(context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li'))
#     todo_items = context.driver.find_elements(By.XPATH, '//ul[@class="todo-list"]/li')
#     assert len(todo_items) == initial_todo_count, "The Todo list was unexpectedly changed."


# @then('the item "{item}" has a strikethrough style')
# def step_then_item_has_strikethrough(context, item):
#     label = context.browser.find_element(
#         By.XPATH, f'//ul[@class="todo-list"]/li[.//label[text()="{item}"]]/label'
#     )
#     text_decoration = label.value_of_css_property("text-decoration-line")
#     assert text_decoration == "line-through", f'Item "{item}" does not have a strikethrough style.'
#

# @then('the Todos labeled "{item1}" and "{item2}" are removed from the list')
# def step_then_items_removed(context, item1, item2):
#     todo_items = context.browser.find_elements(By.XPATH, "//ul[@class='todo-list']/li")
#     remaining_items = [todo.text for todo in todo_items]
#
#     # Check if the deleted items are removed
#     assert item1 not in remaining_items, f'The item "{item1}" was not removed.'
#     assert item2 not in remaining_items, f'The item "{item2}" was not removed.'

@when('the user double-clicks on a Todo item labeled "Buy groceries"')
def step_when_user_dblclicks_todo_item(context):
    todo_item = context.driver.find_element(By.XPATH, '//label[text()="Buy groceries"]')

    # Perform double-click action
    actions = ActionChains(context.driver)
    actions.double_click(todo_item).perform()
    time.sleep(2)

    value_to_paste = "Buy groceries and cook"

    # Copy the value to the clipboard using pyperclip
    pyperclip.copy(value_to_paste)
    logging.info("before control a")
    ActionChains(context.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    logging.info("before control v")
    # Perform Ctrl+V to paste the value from clipboard
    ActionChains(context.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    logging.info("after v")
    time.sleep(5)
    # Optionally, simulate pressing Enter to save the updated Todo item
    todo_item.send_keys(Keys.ENTER)


@when('the user updates the Todo text to "Buy groceries and cook"')
def step_when_user_updates_todo_text(context):
    try:
        # Wait for the Todo item to be visible and clickable
        todo_item = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//ul/li/div[@class='view']/div[@class='input-container']/input[@class='new-todo' and @value='Buy groceries']")
            )
        )

        # Double-click the Todo item to trigger edit mode
        actions = ActionChains(context.driver)
        actions.double_click(todo_item).perform()

        # Wait for the input field to become visible and interactive (without waiting for '.editing')
        # input_box = WebDriverWait(context.driver, 20).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, '.todoapp input.new-todo'))
        # )
        #
        # # Clear the current text and update with new text
        # input_box.clear()
        # input_box.send_keys('Buy groceries and cook')
        #
        # # Optionally, you can simulate pressing "Enter" to finalize the edit
        # input_box.send_keys(Keys.RETURN)
        value_to_paste = "Buy groceries and cook"

        # Copy the value to the clipboard using pyperclip
        pyperclip.copy(value_to_paste)

        edit_input = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li.editing .edit"))
        )
        logging.info("Edit input found, proceeding to edit the todo.")
        # Click into the input field to focus
        edit_input.click()

        # Perform Ctrl+A to select all text
        ActionChains(context.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

        # Perform Ctrl+V to paste the value from clipboard
        ActionChains(context.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        # Optionally, simulate pressing Enter to save the updated Todo item
        edit_input.send_keys(Keys.RETURN)
        # Send the updated text and press Enter to save
        # edit_input.clear()
        # edit_input.send_keys("Buy groceries and cook")
        # edit_input.send_keys(Keys.ENTER)

    except TimeoutException:
        print("Element not found, printing page source for debugging:")
        print(context.driver.page_source)  # Output the HTML for debugging
        raise
    except Exception as e:
        logging.error(f"Error in step 'the user updates the Todo text to': {e}")
        print(context.driver.page_source)  # Output the page HTML for debugging
        capture_screenshot(context.driver, 'the user updates the Todo text to')
        raise e

# @when('the user updates the Todo text to "{new_text}"')
# def step_when_user_updates_todo_text(context, new_text):
#     # Wait for the editing state
#     WebDriverWait(context.driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li.editing"))
#     )
#     # Locate the edit input and send keys
#     edit_input = context.driver.find_element(By.CSS_SELECTOR, ".todo-list li.editing .edit")
#     edit_input.clear()
#     edit_input.send_keys(new_text)
#     edit_input.send_keys(Keys.RETURN)

@when('the user presses Enter')
def step_impl_press_enter(context):
    try:
        # Ensure the Todo item is in editing mode by double-clicking on the Todo label
        todo_label = context.driver.find_element(By.XPATH, '//label[text()="Buy groceries"]')

        # Wait for the label to be clickable and perform a double-click
        WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(todo_label))

        actions = ActionChains(context.driver)
        actions.double_click(todo_label).perform()

        # Wait for the input field to appear after double-clicking
        edit_input = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".todo-list li.editing .edit"))
        )

        # Send the updated text and press Enter to save
        edit_input.clear()
        edit_input.send_keys("Buy groceries and cook")
        edit_input.send_keys(Keys.ENTER)

    except TimeoutException:
        print("Element not found, printing page source for debugging:")
        print(context.driver.page_source)  # Output the HTML for debugging
        capture_screenshot(context.driver, 'the user presses Enter')
        raise
    except Exception as e:
        logging.error(f"Error in step 'the user presses Enter': {e}")
        print(context.driver.page_source)  # Output the page HTML for debugging
        capture_screenshot(context.driver, 'the user presses Enter')
        raise e


@when('update Todo item to "{updated_label}"')
def step_impl_update_todo_item(context, updated_label):
    try:
        # Wait for the editable input field to appear
        edit_input = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.new-todo"))  # Adjust selector as per the observed behavior
        )
        # Clear the input field and type the updated label
        edit_input.clear()
        edit_input.send_keys(updated_label)
        edit_input.send_keys(Keys.ENTER)  # Press Enter to save the changes
    except TimeoutException:
        # Capture the page source for debugging
        page_source = context.driver.page_source
        print("Page source at the time of timeout:", page_source)
        raise AssertionError("Failed to locate the input field for editing")

    time.sleep(5)

@then('the Todo list should still contain {count:d} items')
def step_impl_todo_list_count(context, count):
    try:
        # Locate all todo items
        todo_items = WebDriverWait(context.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.todo-list li"))
        )
        # Assert the number of todo items
        assert len(todo_items) == count, f"Expected {count} items, but found {len(todo_items)}"
    except TimeoutException:
        raise AssertionError("Failed to locate the Todo list or items")
