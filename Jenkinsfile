
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
        bat 'echo Checking Python and pip'
        bat 'where python'
        bat 'python --version'
        bat 'python -m pip --version'
    }
}
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install bandit'

                bat '''
                    if exist requirements.txt (
                        python -m pip install -r requirements.txt
                    )
                '''
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    def scanStatus = bat(
                        returnStatus: true,
                        script: 'python -m bandit -r . -f json -o bandit-report.json -x .git,venv,.venv'
                    )

                    if (scanStatus == 1) {
                        echo 'Security findings detected. Report generated.'
                        currentBuild.result = 'UNSTABLE'
                    } else if (scanStatus != 0) {
                        error("Bandit scan failed with exit code: ${scanStatus}")
                    } else {
                        echo 'Security scan completed successfully.'
                    }
                }
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts(
                    artifacts: 'bandit-report.json',
                    allowEmptyArchive: true
                )
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Check the console output and scan report.'
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        unstable {
            echo 'Pipeline completed with security findings.'
        }

        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
