pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'grafanaw'
        IMAGE_NAME     = 'asdn_project'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install requirements & Test') {
            steps {
                dir('app') {
                    sh 'pip install --no-cache-dir -r requirements.txt'
                    sh 'pytest -q'
                }
            }
        }

        stage('Build Docker image') {
            steps {
                dir('app') {
                    sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER .'
                }
            }
        }

        stage('Push Docker image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker push $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl set image deployment/asdn-project \
                        asdn-project=$DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }
    }
}