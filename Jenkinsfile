pipeline {
  agent any
  environment {
        // Dynamically inject the path to the directory containing python.exe
        PATH = "C:\\Users\\HuyNguyenMinh\\AppData\\Local\\Programs\\Python\\Python314;${env.PATH}"
    }
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python3 hello.py'
      }
    }
  }
}
