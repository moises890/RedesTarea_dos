pipeline {

  agent any
  environment {
    dockerhub=credentials('moises890')
  }
  stages{
    stage('clone repository') {
      steps {
        git([url: 'https://github.com/moises890/RedesTarea_dos.git', branch: 'main'])
      }
    }
    stage('Build docker Image'){
      steps{
        script {
          sh 'docker build -t capa-aplicacion-redes .'
        }
      }
    }
    stage('Push Image'){
      steps{
        script {
          sh 'docker tag capa-aplicacion-redes moises890/capa-aplicacion-redes:latest'
          sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'
          sh 'docker push moises890/capa-aplicacion-redes:latest'
        }
      }
    }
  }
}
