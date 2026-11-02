node {
    try {
        stage('Checkout') {
            echo 'Downloading source code from GitHub'
            checkout scm
        }

        stage('Python Version') {
            bat 'py -3 --version'
        }

        stage('Install Dependencies') {
            bat 'py -3 -m pip install -r requirements.txt'
        }

        stage('Bandit Security Scan') {
            bat 'py -3 -m bandit -r app.py -f json -o bandit-report.json'
        }

        stage('Dependency Vulnerability Scan') {
            bat 'py -3 -m pip_audit -r requirements.txt -f json -o pip-audit-report.json'
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