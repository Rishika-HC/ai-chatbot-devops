pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ai-chatbot"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/Rishika-HC/ai-chatbot-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Run App in Background') {
            steps {
                sh 'nohup python3 app/app.py &'
                sleep 5
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python3 tests/test_selenium.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
            }
        }
    }
}