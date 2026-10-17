pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('automation_selenium') {
      steps {
        bat 'pytest --html reports\report.html testscripts/'
      }
    }
  }
}
