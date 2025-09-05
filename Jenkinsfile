post {
    success {
        echo 'All tests passed!'
        bat """
        python -c "import requests, os; requests.post(
            f'https://api.github.com/repos/szymonpilszak/jenkins-pipeline-python-codewars/statuses/{os.environ['COMMIT']}',
            headers={'Authorization': 'token ' + os.environ['GITHUB_TOKEN'],
                     'Accept': 'application/vnd.github+json'},
            json={'state':'success','description':'All tests passed','context':'Jenkins'}
        )"
        """
    }
    failure {
        echo 'Some tests failed.'
        bat """
        python -c "import requests, os; requests.post(
            f'https://api.github.com/repos/szymonpilszak/jenkins-pipeline-python-codewars/statuses/{os.environ['COMMIT']}',
            headers={'Authorization': 'token ' + os.environ['GITHUB_TOKEN'],
                     'Accept': 'application/vnd.github+json'},
            json={'state':'failure','description':'Tests failed','context':'Jenkins'}
        )"
        """
    }
}
