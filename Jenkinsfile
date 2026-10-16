
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
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Automated Security Scan') {
            steps {
                bat '''
                    set "PYTHON=C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"

                    "%PYTHON%" -m bandit -r . -ll -ii -f json -o bandit-report.json
                    set "BANDIT_EXIT=%ERRORLEVEL%"

                    if "%BANDIT_EXIT%"=="0" (
                        echo No qualifying security findings detected.
                        exit /b 0
                    )

                    if "%BANDIT_EXIT%"=="1" (
                        echo Security findings detected. Review bandit-report.json.
                        exit /b 0
                    )

                    echo Bandit encountered an error. Exit code: %BANDIT_EXIT%
                    exit /b %BANDIT_EXIT%
                '''
            }
        }

        stage('Application Test') {
            steps {
                bat '''
                    set "PYTHON=C:\\Users\\mithu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"

                    if exist app.py (
                        "%PYTHON%" -m py_compile app.py
                        if errorlevel 1 exit /b 1
                        echo Application Python syntax check passed.
                    ) else (
                        echo app.py not found. Application syntax check skipped.
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
            echo 'Pipeline failed. Review the earlier Console Output errors.'
        }
    }
}
