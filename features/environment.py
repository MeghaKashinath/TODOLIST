from selenium import webdriver
import os

def before_all(context):
    # Initialize WebDriver (use Chrome, for example)
    context.driver = webdriver.Chrome()
    context.driver.get("https://todomvc.com/examples/react/dist#/")  # Open the TodoMVC app

    # Create or open a report file
    report_file_path = os.path.join(os.getcwd(), "test_report.html")  # Save report in the current directory
    context.report_file = open(report_file_path, "w")

    # Write the initial content for an HTML report
    context.report_file.write("<html><head><title>Test Report</title></head><body>")
    context.report_file.write("<h1>TodoMVC Test Execution Report</h1>")
    context.report_file.write("<table border='1'><tr><th>Scenario</th><th>Status</th></tr>")

def after_scenario(context, scenario):
    # Log each scenario's result into the report
    status = "PASSED" if scenario.status == "passed" else "FAILED"
    context.report_file.write(f"<tr><td>{scenario.name}</td><td>{status}</td></tr>")

def after_all(context):
    # Cleanup after all tests
    context.report_file.write("</table></body></html>")  # Close the HTML content
    context.report_file.close()  # Close the report file
    context.driver.quit()  # Close the browser after tests are finished
