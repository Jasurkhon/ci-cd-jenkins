pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ml-model'
        CONTAINER_NAME = 'ml-model-container'
        DOCKER_PORT = '8000:8000'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh '''
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }
        
        stage('Test Docker Image') {
            steps {
                echo 'Running Docker Container for Testing...'
                sh '''
                    docker run --rm -d --name ${CONTAINER_NAME} -p ${DOCKER_PORT} ${IMAGE_NAME}
                    sleep 5 # Wait for the container to initialize
                    curl --fail http://0.0.0.0:8000 || (echo "Service failed to respond" && exit 1)
                '''
            }
        }

        stage('Cleanup Test') {
            steps {
                echo 'Cleaning up test container...'
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh '''
                    # Adjust deployment commands for your target environment
                    docker run -d --name ${CONTAINER_NAME}-prod -p ${DOCKER_PORT} ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up dangling Docker images...'
            sh '''
                docker image prune -f
            '''
        }
    }
}
