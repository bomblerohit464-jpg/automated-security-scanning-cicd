
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Security Scanner') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Automated Security Scan') {
            steps {
                bat 'python -m bandit -r . -ll -ii -f json -o bandit-report.json'
            }
        }

        stage('Application Test') {
            steps {
                bat 'python app.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'bandit-report.json',
                             allowEmptyArchive: true
        }
    }
}
