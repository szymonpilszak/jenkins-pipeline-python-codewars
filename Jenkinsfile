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
            withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                bat '''
                set COMMIT=%GIT_COMMIT%
                curl -H "Authorization: token %GITHUB_TOKEN%" ^
                     -H "Accept: application/vnd.github+json" ^
                     -d "{\\"state\\":\\"success\\",\\"description\\":\\"All tests passed\\",\\"context\\":\\"Jenkins\\"}" ^
                     https://api.github.com/repos/szymonpilszak/jenkins-pipeline-python-codewars/statuses/%COMMIT%
                '''
            }
        }
        failure {
            echo 'Some tests failed.'
            withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                bat '''
                set COMMIT=%GIT_COMMIT%
                curl -H "Authorization: token %GITHUB_TOKEN%" ^
                     -H "Accept: application/vnd.github+json" ^
                     -d "{\\"state\\":\\"failure\\",\\"description\\":\\"Tests failed\\",\\"context\\":\\"Jenkins\\"}" ^
                     https://api.github.com/repos/szymonpilszak/jenkins-pipeline-python-codewars/statuses/%COMMIT%
                '''
            }
        }
    }
}
