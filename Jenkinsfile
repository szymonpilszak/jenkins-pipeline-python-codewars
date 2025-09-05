pipeline {
    agent any

    environment {
        
        GITHUB_TOKEN = credentials('github-token')
        PYTHON_PATH = "C:\\Users\\szymo\\AppData\\Local\\Programs\\Python\\Python310\\"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                bat "echo %PYTHON_PATH%;C:\\Program Files\\Git\\cmd;C:\\Users\\szymo\\AppData\\Local\\Programs\\Python\\Python310\\Scripts;%PATH%"
                bat "python --version"
            }
        }

        stage('Run Tests') {
            steps {
                bat "python -m unittest discover tests"
            }
        }
    }

    post {
        success {
            githubNotify(
                context: 'CI',
                description: 'Build passed',
                status: 'SUCCESS',
                repo: 'szymonpilszak/jenkins-pipeline-python-codewars',
                account: 'szymonpilszak',
                credentialsId: 'github-token-id'
            )
            echo 'Build finished successfully!'
        }

        failure {
            githubNotify(
                context: 'CI',
                description: 'Build failed',
                status: 'FAILURE',
                repo: 'szymonpilszak/jenkins-pipeline-python-codewars',
                account: 'szymonpilszak',
                credentialsId: 'github-token'
            )
            echo 'Build failed!'
        }
    }
}
