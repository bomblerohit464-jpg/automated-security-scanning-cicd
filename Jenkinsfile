
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading source code from GitHub'
                checkout scm
                echo 'GitHub checkout completed!'
            }
        }

        stage('Python Version') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies'
                bat '"%PYTHON%" -m pip install -r requirements.txt'
                echo 'Dependencies installed successfully'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                echo 'Starting Bandit Security Scan'

                script {
                    def result = bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m bandit -r app.py -f screen'
                    )

                    bat '"%PYTHON%" -m bandit -r app.py -f json -o bandit-report.json'

                    if (result == 0) {
                        echo 'Bandit scan completed without detected issues.'
                    } else {
                        echo 'Bandit detected security findings. Check the report.'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Dependency Vulnerability Scan') {
            steps {
                echo 'Starting dependency vulnerability scan'

                script {
                    def result = bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m pip_audit -r requirements.txt'
                    )

                    bat '"%PYTHON%" -m pip_audit -r requirements.txt -f json -o pip-audit-report.json'

                    if (result == 0) {
                        echo 'No known dependency vulnerabilities found.'
                    } else {
                        echo 'Dependency vulnerabilities detected. Check the report.'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Build Successful') {
            steps {
                echo '======================================'
                echo ' AUTOMATED SECURITY SCANNING'
                echo '======================================'
                echo 'Python Application: Checked'
                echo 'Bandit Security Scan: Completed'
                echo 'Dependency Scan: Completed'
                echo '======================================'
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: '*-report.json',
                allowEmptyArchive: true
            )
            echo 'Security scan reports archived in Jenkins.'
        }

        success {
            echo 'PROJECT PIPELINE COMPLETED SUCCESSFULLY!'
        }

        unstable {
            echo 'Pipeline completed with security findings. Review reports.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for errors.'
        }
    }
}
