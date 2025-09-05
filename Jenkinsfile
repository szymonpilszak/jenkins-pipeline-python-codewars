pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pobranie kodu z GitHuba
                git branch: 'main',
                    url: 'https://github.com/szymonpilszak/jenkins-pipeline-python-codewars.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Upewniamy się, że pip jest aktualny
                sh 'python -m pip install --upgrade pip || true'

                // Instalacja zależności, jeśli plik requirements.txt istnieje
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                // Odpalenie wszystkich testów w katalogu tests/
                sh 'python -m unittest discover tests'
            }
        }
    }

    post {
        always {
            // Tutaj można dodać raportowanie testów, np. JUnit XML, jeśli będziesz generować
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