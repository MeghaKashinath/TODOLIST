pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/MeghaKashinath/TODOLIST.git'
            }
        }
        stage('Setup Environment') {
            steps {
                // Install dependencies
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run test cases
                sh 'python3 test_runner.py'
            }
        }
    }
}
