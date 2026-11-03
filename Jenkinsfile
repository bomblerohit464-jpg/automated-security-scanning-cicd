
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        APP_URL = 'http://127.0.0.1:5000'
    }

    stages {

        stage('Checkout') {
            steps {
                echo '======================================'
                echo 'DOWNLOADING SOURCE CODE FROM GITHUB'
                echo '======================================'

                checkout scm

                echo 'GitHub checkout completed successfully!'
            }
        }

        stage('Python Version') {
            steps {
                echo 'Checking Python version'
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies'

                bat '"%PYTHON%" -m pip install -r requirements.txt'

                echo 'Dependencies installed successfully!'
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

                    bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m bandit -r app.py -f json -o bandit-report.json'
                    )

                    if (result == 0) {
                        echo 'Bandit scan completed without detected issues.'
                    } else {
                        echo 'Security findings detected. Check the report.'
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

                    bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m pip_audit -r requirements.txt -f json -o pip-audit-report.json'
                    )

                    if (result == 0) {
                        echo 'No known dependency vulnerabilities found.'
                    } else {
                        echo 'Dependency vulnerabilities detected.'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Build Successful') {
            steps {
                echo '======================================'
                echo 'AUTOMATED SECURITY SCANNING PROJECT'
                echo '======================================'

                echo 'Python Application: Checked'
                echo 'Bandit Security Scan: Completed'
                echo 'Dependency Scan: Completed'

                echo 'Build process completed!'
            }
        }

        stage('Application URL') {
            steps {
                echo '======================================'
                echo 'FLASK APPLICATION ADDRESS'
                echo '======================================'

                echo 'Open your browser using:'
                echo 'http://127.0.0.1:5000'

                echo 'Note: Flask must be running separately.'
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

            echo 'Security reports archived successfully.'
        }

        success {
            echo 'PROJECT PIPELINE COMPLETED SUCCESSFULLY!'
        }

        unstable {
            echo 'Pipeline completed with security findings.'
            echo 'Please review the archived reports.'
        }

        failure {
            echo 'PIPELINE FAILED!'
            echo 'Check Jenkins Console Output.'
        }
    }
}
