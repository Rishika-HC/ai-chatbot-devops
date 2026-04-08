# AI Chatbot DevOps Project

## Features
- Flask AI Chatbot
- OpenRouter API integration
- Docker containerization
- Jenkins CI/CD pipeline
- Selenium testing

## Run Locally
pip install -r app/requirements.txt
python app/app.py

## Docker
docker build -t ai-chatbot .
docker run -p 5000:5000 ai-chatbot