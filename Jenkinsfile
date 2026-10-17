pipeline {
  agent any
  stages {
    stage('automation_selenium') {
      steps {
        bat 'pytest --html reports\\report.html testscripts/'
      }
    }
  }
}
