pipeline {
    agent any

    environment {
        // Wstaw tutaj ID poświadczenia, które dodałeś w Jenkinsie
        GITHUB_TOKEN = credentials('github-token')
        REPO_OWNER = 'szymonpilszak'
        REPO_NAME = 'jenkins-pipeline-python-codewars'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: "https://github.com/${env.REPO_OWNER}/${env.REPO_NAME}.git"
            }
        }

        stage('Check Environment') {
            steps {
                bat 'echo %PATH%'
                bat 'python --version'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest discover tests'
            }
        }
    }

    post {
        success {
            // Zgłaszanie sukcesu do GitHub
            githubNotify context: 'Jenkins', status: 'SUCCESS', description: 'All tests passed'
            echo 'All tests passed!'
        }
        failure {
            // Zgłaszanie błędu do GitHub
            githubNotify context: 'Jenkins', status: 'FAILURE', description: 'Some tests failed'
            echo 'Some tests failed.'
        }
        always {
            echo 'Build finished!'
        }
    }
}
