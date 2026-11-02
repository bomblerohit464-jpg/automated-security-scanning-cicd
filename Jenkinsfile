pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading source code from GitHub'
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat 'py -3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -3 -m pip install -r requirements.txt'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                bat 'py -3 -m bandit -r app.py -f json -o bandit-report.json'
            }
        }

        stage('Dependency Vulnerability Scan') {
            steps {
                bat 'py -3 -m pip_audit -r requirements.txt -f json -o pip-audit-report.json'
            }
        }

        stage('Build Successful') {
            steps {
                echo 'Automated Security Scanning Completed'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*-report.json',
                             allowEmptyArchive: true
        }
    }
}