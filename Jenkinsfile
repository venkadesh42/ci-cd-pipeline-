pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                checkout scm
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    python3 -m py_compile app.py
                    echo "Application test passed"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t devops-webapp:latest .
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker stop devops-webapp || true
                    docker rm devops-webapp || true

                    docker run -d \
                      --name devops-webapp \
                      -p 5000:5000 \
                      devops-webapp:latest

                    echo "Application deployed successfully"
                '''
            }
        }

        stage('Verify Application') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD PIPELINE COMPLETED SUCCESSFULLY'
        }

        failure {
            echo 'CI/CD PIPELINE FAILED'
        }
    }
}
