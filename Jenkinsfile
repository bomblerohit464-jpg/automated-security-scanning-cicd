
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    mkdir -p reports
                    .venv/bin/bandit -r . \
                      -x ./.venv \
                      -f json \
                      -o reports/bandit-report.json
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/**',
                                 allowEmptyArchive: false
            }
        }
    }

    post {
        success {
            echo 'Security scan passed.'
        }
        failure {
            echo 'Pipeline failed. Check the console output and scan report.'
        }
    }
}
