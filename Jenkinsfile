pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ai-chatbot"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Rishika-HC/ai-chatbot-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\rishi\\anaconda3\\python.exe -m pip install -r app\\requirements.txt'
            }
        }

        stage('Run App in Background') {
    steps {
        bat 'start /B C:\\Users\\rishi\\anaconda3\\python.exe app\\app.py'
        sleep 5
    }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'C:\\Users\\rishi\\anaconda3\\python.exe tests\\test_selenium.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f ai-chatbot'
                bat 'docker run -d -p 5000:5000 --name ai-chatbot %DOCKER_IMAGE%'
            }
        }
    }
}
