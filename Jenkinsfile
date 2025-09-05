pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/szymonpilszak/jenkins-pipeline-python-codewars.git'
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
        always {
            echo 'Build finished!'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
