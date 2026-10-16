
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
                bat '''
                    set "PYTHON=C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
                    "%PYTHON%" --version
                    "%PYTHON%" -m pip --version
                '''
            }
        }

        stage('Install Security Scanner') {
            steps {
                bat '''
                    set "PYTHON=C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
                    "%PYTHON%" -m pip install bandit
                '''
            }
        }

        
        stage('Automated Security Scan') {
            steps {
                bat '''
                    set "PYTHON=C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"

                    "%PYTHON%" -m bandit -r . -ll -ii -f json -o bandit-report.json

                    if errorlevel 2 exit /b %ERRORLEVEL%
                    if errorlevel 1 echo Security findings detected. Continuing to archive the report.
                    exit /b 0
                '''
            }
        }

        

        stage('Application Test') {
            steps {
                bat '''
                    set "PYTHON=C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
                    if exist app.py (
                        "%PYTHON%" app.py
                    ) else (
                        echo app.py not found - skipping application test
                    )
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'bandit-report.json',
                allowEmptyArchive: true
            )
            echo 'Security scanning pipeline finished.'
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
