pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        sh 'ls -ltr'
        sh 'docker --version'
        sh 'docker ps'
      }
    }

    stage('build') {
      steps {
        sh './build.sh'
      }
    }

  }
}