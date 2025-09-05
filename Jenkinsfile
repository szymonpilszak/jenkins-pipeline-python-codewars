pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github-token')
        PYTHON_HOME = "C:\\Users\\szymo\\AppData\\Local\\Programs\\Python\\Python310"
        GIT_HOME    = "C:\\Program Files\\Git\\cmd"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Get Commit SHA') {
            steps {
                script {
                    // Pobranie SHA aktualnego commita
                    commitSha = bat(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    echo "Commit SHA: ${commitSha}"
                }
            }
        }

        stage('Check Environment') {
            steps {
                script {
                    // Ustawienie PATH w prosty sposób
                    env.PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${GIT_HOME};${env.PATH}"
                    bat "echo %PATH%"
                    bat "python --version"
                    bat "git --version"
                }
            }
        }

        stage('Test Credentials') {
            steps {
                script {
                    // Sprawdzenie, czy Jenkins widzi token
                    def secret = credentials('github-token')
                    if (secret) {
                        echo "Secret is set!"
                    } else {
                        echo "Secret NOT found!"
                    }
                }
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
                sha: commitSha,
                credentialsId: 'github-token'
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
                sha: commitSha,
                credentialsId: 'github-token'
            )
            echo 'Build failed!'
        }
    }
}
