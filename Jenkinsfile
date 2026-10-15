pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        // Change this to the actual Python executable on your PC.
        PYTHON = 'C:\\Path\\To\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Prepare Reports') {
            steps {
                bat 'if not exist reports mkdir reports'
            }
        }

        stage('Bandit Security Scan') {
            steps {
                script {
                    int result = bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m bandit -r . -x .\\venv,.\\.git,.\\reports -f json -o reports\\bandit-report.json'
                    )

                    if (result != 0) {
                        echo "Bandit returned exit code ${result}. Review the report."
                    }
                }
            }
        }

        stage('Dependency Audit') {
            steps {
                script {
                    int result = bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m pip_audit -r requirements.txt -f json -o reports\\pip-audit.json'
                    )

                    if (result != 0) {
                        echo "Dependency audit returned exit code ${result}. Review the report."
                    }
                }
            }
        }

        stage('Application Health Check') {
            steps {
                bat '"%PYTHON%" -m compileall -q app.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'reports/*.json',
                allowEmptyArchive: true
            )
        }

        success {
            echo 'Pipeline stages completed.'
        }

        failure {
            echo 'A pipeline stage failed. Review the Jenkins console output.'
        }
    }
}
