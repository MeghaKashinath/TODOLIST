import logging
import os
from selenium import webdriver
from datetime import datetime

def setup_logging():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)  # Create logs directory if it doesn't exist
    log_file_path = os.path.join(log_dir, 'test_execution.log')  # Path for log file
    print(f"Log file path: {log_file_path}")  # Debugging print statement

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Create file handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Set formatter for both handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Capture a screenshot in case of an error
def capture_screenshot(driver, scenario_name):
    screenshot_dir = 'screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)  # Create screenshots directory if it doesn't exist
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_dir, f"{scenario_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    logging.info(f"Screenshot captured: {screenshot_path}")

# Function to initialize the WebDriver
def init_driver(browser_type='chrome'):
    # Determine which browser to use
    if browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()  # Assumes chromedriver is in PATH
    elif browser_type.lower() == 'firefox':
        driver = webdriver.Firefox()  # Assumes geckodriver is in PATH
    else:
        raise ValueError(f"Unsupported browser: {browser_type}")
    return driver

def before_all(context):
    setup_logging()  # Setup logging for the entire test session
    # Get browser choice from environment or default to Chrome
    browser = os.getenv('BROWSER', 'chrome').lower()
    # Initialize WebDriver
    # context.driver = webdriver.Chrome()
    # Initialize WebDriver based on browser choice

    context.driver = init_driver(browser)
    context.driver.get("https://todomvc.com/examples/react/dist#/")  # Open the TodoMVC app

    # Create or open a report file
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)  # Create the 'reports' folder if it doesn't exist
    report_file_path = os.path.join(report_dir, "test_report.html")
    context.report_file = open(report_file_path, "w")

    # Write the initial content for an HTML report
    context.report_file.write("<html><head><title>Test Report</title></head><body>")
    context.report_file.write("<h1>TodoMVC Test Execution Report</h1>")
    context.report_file.write("<table border='1'><tr><th>Scenario</th><th>Status</th><th>Timestamp</th></tr>")

def after_scenario(context, scenario):
    # Log each scenario's result into the report
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp
    status = "PASSED" if scenario.status == "passed" else "FAILED"
    # Log the scenario status to the log file
    logging.info(f"Scenario '{scenario.name}' finished with status: {status} at {timestamp}")

    context.report_file.write(f"<tr><td>{scenario.name}</td><td>{status}</td><td>{timestamp}</td></tr>")

def after_all(context):
    # Cleanup after all tests
    logging.info("Test suite execution completed.")
    context.report_file.write("</table></body></html>")  # Close the HTML content
    context.report_file.close()  # Close the report file
    context.driver.quit()  # Close the browser after tests are finished
    logging.info("Browser session ended and resources cleaned up.")

