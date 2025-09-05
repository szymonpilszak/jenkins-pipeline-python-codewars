Latest CI status here:
[![Build Status](https://github.com/szymonpilszak/jenkins-pipeline-python-codewars/actions/workflows/ci.yml/badge.svg)](https://github.com/szymonpilszak/jenkins-pipeline-python-codewars/actions/workflows/ci.yml)


# Jenkins + GitHub Actions CI for Python Codewars

A collection of Codewars solutions in Python with simple unit tests.  .

This project uses **Jenkins** for local CI and **GitHub Actions** for public CI visibility.


## Local Jenkins

Jenkins is running **locally on my machine**. Because the server is not publicly accessible, the build status cannot be directly shown in this README.  

To see the Jenkins build output, I attach **screenshots of the latest build** for each commit. These screenshots show that all tests pass or fail as expected.


## GitHub Actions

For public visibility, the same tests are run automatically on GitHub Actions for every commit to the `main` branch.  

<img width="1850" height="902" alt="image" src="https://github.com/user-attachments/assets/97d77df0-6d51-411e-b46a-2a43782413aa" />


## How it works

1. **Local Jenkins** runs the pipeline with Python 3.10 and unittests.
2. **Screenshots** of Jenkins builds are attached to commits for documentation.
3. **GitHub Actions** runs the same tests automatically on push and pull requests to `main`.
