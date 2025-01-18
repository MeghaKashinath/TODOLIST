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
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 test_runner.py 
```


For setting up Firefox browser set BROWSER env to firefox
```bash
  export BROWSER=firefox
```