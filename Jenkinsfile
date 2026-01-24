pipeline {
    agent any

    environment {
        IMAGE_REPO = "grafanaw/asdn_project"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        IMAGE      = "${IMAGE_REPO}:${IMAGE_TAG}"
        IMAGE_LATEST = "${IMAGE_REPO}:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build App Image') {
            steps {
                dir('app') {
                    sh """
                      docker build -t ${IMAGE} -t ${IMAGE_LATEST} .
                    """
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                // شغّل pytest من داخل /app لأن هناك موجود tests وsrc بالصورة
                sh "docker run --rm -w /app -e PYTHONPATH=/app $IMAGE pytest -q"

            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh """
                      echo "${PASS}" | docker login -u "${USER}" --password-stdin
                      docker push ${IMAGE}
                      docker push ${IMAGE_LATEST}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
  steps {
    withCredentials([string(credentialsId: 'k8s-jenkins-token', variable: 'K8S_TOKEN')]) {
      sh '''
        kubectl \
          --server="https://kubernetes.docker.internal:6443" \
          --token="$K8S_TOKEN" \
          --insecure-skip-tls-verify=true \
          apply -f k8s/ \
          --validate=false
      '''
    }
  }
}


    }
}
