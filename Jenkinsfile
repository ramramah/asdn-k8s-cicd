pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    IMAGE_REPO   = "grafanaw/asdn_project"
    IMAGE_TAG    = "${BUILD_NUMBER}"
    IMAGE        = "${IMAGE_REPO}:${IMAGE_TAG}"
    IMAGE_LATEST = "${IMAGE_REPO}:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        retry(2) {
          checkout scm
        }
      }
    }

    stage('Build App Image') {
      steps {
        dir('app') {
          sh 'docker build -t ${IMAGE} -t ${IMAGE_LATEST} .'
        }
      }
    }

    stage('Run Tests in Docker') {
      steps {
        dir('app') {
          sh 'docker run --rm -w /app -e PYTHONPATH=/app ${IMAGE} pytest -q'
        }
      }
    }

    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
          usernameVariable: 'USER',
          passwordVariable: 'PASS'
        )]) {
          sh '''
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker push ${IMAGE}
            docker push ${IMAGE_LATEST}
          '''
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG_FILE')]) {
          sh '''
            kubectl --kubeconfig="$KUBECONFIG_FILE" cluster-info
            kubectl --kubeconfig="$KUBECONFIG_FILE" get nodes
            kubectl --kubeconfig="$KUBECONFIG_FILE" apply -f k8s/ --validate=false
          '''
        }
      }
    }
  }
}
