Latest CI status here:
[![Build Status](https://github.com/szymonpilszak/jenkins-pipeline-python-codewars/actions/workflows/ci.yml/badge.svg)](https://github.com/szymonpilszak/jenkins-pipeline-python-codewars/actions/workflows/ci.yml)


# Jenkins + GitHub Actions CI for Python Codewars

A collection of Codewars solutions in Python with simple unit tests.  .

This project uses **Jenkins** for local CI and **GitHub Actions** for public CI visibility.


## Local Jenkins

Jenkins is running **locally on my machine**. Because the server is not publicly accessible, the build status cannot be directly shown in this README.  

To see the Jenkins build output, I attach **screenshots of the latest build** for each commit. These screenshots show that all tests pass or fail as expected.
<img width="1896" height="1693" alt="image" src="https://github.com/user-attachments/assets/591eebc0-45d5-4bd1-9803-6900727dff8f" />




## GitHub Actions

For public visibility, the same tests are run automatically on GitHub Actions for every commit to the `main` branch.  


## How it works

1. **Local Jenkins** runs the pipeline with Python 3.10 and unittests. Screenshots of Jenkins builds can be added to the repository manually for documentation.
2. **Screenshots** of Jenkins builds are added to the repository manually for documentation.
3. **GitHub Actions** runs the same tests automatically on push and pull requests to `main`.


## TODO IN FUTURE
1. **Public server with docker**  to run pipeline independently from my localhost.
