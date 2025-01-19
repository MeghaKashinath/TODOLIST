READ ME FILE
# Todo List Automation Project

## Overview
This project automates the testing of a Todo List web application using Behave (BDD framework) and Selenium.

## Features
- Add, Edit, and Delete Todos
- Mark Todos as Completed
- Filter Todos by status (Active/Completed)

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