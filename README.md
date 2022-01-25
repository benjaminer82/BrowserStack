<h1 align="center">Welcome to Kai's BrowserStack Test Project 👋</h1>
<p align="center">
</p>

> Test scripts setup to run on the automation service, BrowserStack. <br /> Can also be used directly through `Jenkins projects`.

## ✨ Demo Workflow

Full process from `Jenkins Pipeline` to `BrowserStack Test Automation` with test scripts running in parralell:

![image](https://user-images.githubusercontent.com/8535941/150889063-3a48435b-09b6-444c-9446-a1358fb335ef.png)

<p align="center">
  <img width="700" align="center" src="https://user-images.githubusercontent.com/8535941/150889063-3a48435b-09b6-444c-9446-a1358fb335ef.png" alt="demo"/>
</p>

## ✨ Jenkins Pipeline Configuration

![Jenkins pipeline](https://user-images.githubusercontent.com/8535941/150889740-723949de-09f1-4ece-9287-a8af20640bfe.gif)

<p align="center">
  <img width="700" align="center" src="https://user-images.githubusercontent.com/8535941/150889740-723949de-09f1-4ece-9287-a8af20640bfe.gif" alt="Jenkins Pipeline Configuration"/>
</p>

Example of `Jenkins Pipeline Script` with groovy:

```groovy
pipeline {
    agent any

    stages {
        stage('CheckOut') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://***GitHubAuthToken***@github.com/benjaminer82/BrowserStack.git/']]])
            }
        }
        stage('Run Tests') {
            parallel{
                stage('Test on OSX') {
                    steps {
                    sh 'python3 testOSXChrome.py'
                    }
                }
                stage('Test On Windows 11 Edge') {
                    steps {
                        sh 'python3 testWindows11Edge.py'
                    }
                }
                stage('Test On iOS') {
                    steps {
                        sh 'python3 testiOSiPhone13.py'
                    }
                }
                stage('Test On Windows 10 Firefox') {
                    steps {
                        sh 'python3 testWindows10Firefox.py'
                    }
                }
                stage('Test On iPad Air 4') {
                    steps {
                        sh 'python3 testiOSiPadAir4.py'
                    }
                }
            }
        }
    }
}
```

## ✨ Individual Test on BrowserStack

![individual test](https://user-images.githubusercontent.com/8535941/150889554-b69179be-b76f-4ab3-b5ea-b062986dbe8b.gif)

<p align="center">
  <img width="700" align="center" src="https://user-images.githubusercontent.com/8535941/150889554-b69179be-b76f-4ab3-b5ea-b062986dbe8b.gif" alt="Individual Test on BrowserStack"/>
</p>


## 🚀 Usage

This is a demo project showcase the workflow from Jenkins to BrowserStack. It can be used to automate the test process for any web application using a test suite/framework like Selenium.
