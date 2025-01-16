from selenium import webdriver
import os
from datetime import datetime

def before_all(context):
    # Initialize WebDriver (use Chrome, for example)
    context.driver = webdriver.Chrome()
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
    context.report_file.write(f"<tr><td>{scenario.name}</td><td>{status}</td><td>{timestamp}</td></tr>")

def after_all(context):
    # Cleanup after all tests
    context.report_file.write("</table></body></html>")  # Close the HTML content
    context.report_file.close()  # Close the report file
    context.driver.quit()  # Close the browser after tests are finished
