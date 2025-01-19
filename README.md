READ ME FILE
# Todo List Automation Project

## Overview
This project automates the testing of a Todo List web application using Behave (BDD framework) and Selenium.

## Features
- Add, and Delete Todos
- Mark Todos as Completed
- Filter Todos by status (All/Active/Completed)

## Tech Stack
- **Programming Language:** Python
- **Test Framework:** Behave
- **Browser Automation:** Selenium WebDriver
- **logging:** Python's built-in logging module  
- **Reports:** HTML

## Prerequisites
- Python 3.x
- Google Chrome and Chromedriver
- Firefox driver
- Install dependencies using:
```bash
  pip3 install -r requirements.txt
```

Follow below steps to setup and execute the framework.
```bash
    git clone <repo_url>
    cd <repo_dir>
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 test_runner.py 
```

By default, this will run on the chrome browser.
For setting up Firefox browser set BROWSER env to firefox
```bash
  export BROWSER=firefox
  python3 test_runner.py
```

Once all the scenarios are executed, a HTML report is generated under **reports** folder and all related screenshots are stored under screenshots **folder**.
The logs test execution details to both the console and a file named *test_execution.log* located under the logs directory.

The logs include:
* Test execution milestones (e.g., scenario start/end).
* Scenario statuses (PASSED/FAILED).
* Any captured screenshots during test failures.

## Jenkins Pipeline for Automated Testing

This project includes a Jenkins pipeline to automate the execution of the test framework on different browsers (Chrome and Firefox) and archive the test reports. The pipeline is designed to set up the environment, execute the tests, and store the results for analysis.

### How to Use
* Ensure Jenkins is installed and configured to work with your repository.
* Add this **Jenkinsfile** to the root directory of your project.
* Configure a Jenkins job to use the pipeline script:
  * Select "Pipeline" as the project type.
  * Point to this Jenkinsfile in your repository.
* Trigger the pipeline to:
  * Set up the environment.
  * Run tests on both Chrome and Firefox.
  * Archive the test reports for review.

This pipeline simplifies continuous integration by automating the testing process and providing detailed reports for analysis.
