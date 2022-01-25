<h1 align="center">Welcome to Kai's BrowserStack Test Project 👋</h1>
<p align="center">
</p>

> This project contains 5 test scripts set up to run on the test automation platform, `BrowserStack`. 
> <br /> Ready to be used directly through `Jenkins projects`.
> <br />All five scripts have the same set of tests on a demo website to make sure it is running correctly. 
<br /> There're `3 seperate assertions` in each script to test the following scenario

| # | Assertion Scenario        | 
|---|---------------------------|
| 1 | Check page title          | 
| 2 | Make sure the first item is an iPhone 12   |
| 3 | Make sure the item has been correctly added into cart      | 



Five test scripts were created to run separately on the following platforms & browsers to test the cross platform/browser suitability.

| # | File Name                 | Platform  | Browser |
|---|---------------------------|:---------:|-------------|
| 1 | testOSXChrome.py          | Mac OSX   | Chrome |
| 2 | testWindows10Firefox.py   | Window 10 | Firefox |
| 3 | testWindows11Edge.py      | Windows 11| Edge |
| 4 | testiOSiPadAir4.py        | iOS  | iPad default |
| 5 | testiOSiPhone13.py        | iOS  | iPhone default |



## ✨ Demo Workflow

Below is a demo for full process from executing a `Jenkins Pipeline` to testing jobs triggered on `BrowserStack Test Automation platform`.
<br />All 5 test scripts running in `parallel`:

<p align="center">
  <img width="800" align="center" src="https://user-images.githubusercontent.com/8535941/150890222-2b31550b-b54e-46c1-afa9-24b38b020f66.gif" alt="demo"/>
</p>



## ✨ Jenkins Pipeline Configuration

The Jenkins pipeline configuration used for the demo above.

<p align="center">
  <img width="800" align="center" src="https://user-images.githubusercontent.com/8535941/150889740-723949de-09f1-4ece-9287-a8af20640bfe.gif" alt="Jenkins Pipeline Configuration"/>
</p>


#### Example of `Jenkins Pipeline Script` with groovy:<br />

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

<p align="center">
  <img width="800" align="center" src="https://user-images.githubusercontent.com/8535941/150889554-b69179be-b76f-4ab3-b5ea-b062986dbe8b.gif" alt="Individual Test on BrowserStack"/>
</p>


## 🚀 Usage

This is a demo project showcase the workflow from Jenkins to BrowserStack. It can be used to automate the test process for any web application using a test suite/framework like Selenium.
