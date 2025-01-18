pipeline {
    agent any
    environment {
        // You can define BROWSER as an environment variable here
        // For running on Chrome
        CHROME_BROWSER = 'chrome'
        FIREFOX_BROWSER = 'firefox'
    }
    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests on Chrome') {
            environment {
                BROWSER = "${CHROME_BROWSER}"
            }
            steps {
                sh '''
                . venv/bin/activate
                python3 test_runner.py
                '''
            }
        }
        stage('Run Tests on Firefox') {
            environment {
                BROWSER = "${FIREFOX_BROWSER}"
            }
            steps {
                sh '''
                . venv/bin/activate
                python3 test_runner.py
                '''
            }
        }
    }
}
