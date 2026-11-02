node {
    try {
        stage('Checkout') {
            echo 'Downloading source code from GitHub'
            checkout scm
        }

        stage('Python Version') {
            bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
        }

        stage('Install Dependencies') {
            bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
        }

        stage('Bandit Security Scan') {
            bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m bandit -r app.py -f json -o bandit-report.json'
        }

        stage('Dependency Vulnerability Scan') {
            bat '"C:\\Users\\rohit\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip_audit -r requirements.txt -f json -o pip-audit-report.json'
        }

        stage('Build Successful') {
            echo 'Automated Security Scanning Completed'
        }
    }
    finally {
        archiveArtifacts artifacts: '*-report.json',
                         allowEmptyArchive: true
    }
}