# Emotion-Detector
- Clone Count: [PLACEHOLDER]
- Visit Count: [PLACEHOLDER]

## Description
This repository contains an Emotion Detection system designed to process customer feedback in text format and analyze the emotions expressed. The system is intended to be used for performing analytics on customer feedback for signature products, helping businesses gain insights into customer sentiment and improve their offerings based on emotional responses.

## Features
- Emotion analysis of text data
- Use of pre-trained Hugging Face transformer model for emotion detection
- Flask-based web server for interaction

## Demo 
To see a demo of the Emotion-Detector in action, watch the following YouTube video:

[![Emotion-Detector Demo](https://img.youtube.com/vi/iPis4YlMZq0/0.jpg)](https://youtu.be/iPis4YlMZq0)

## Installation and Usage
Step 1: Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo-name.git
```

Step 2: Navigate to the Project Directory
Go into the project directory:
```bash
cd Emotion-Detector
```

Then, you have 2 options:

- Option 1: Using Docker
If you prefer to use Docker to run the application, follow these steps:

    Step 3: Build the Docker Image Run the following command to build the Docker image:
    ```bash
    docker build -t emotion-detector .
    ```

    Step 4: Run the Docker Container Start the container with the following command:
    ```bash
    docker run -p 5000:5000 emotion-detector
    ```
- Option 2: Without Docker (Using Virtual Environment)
If you don't want to use Docker, you can set up a virtual environment and run the application locally. Here's how:

    Step 3: Set Up Virtual Environment
    If you don't have virtualenv installed, you can install it first
    Refers to this article:[Why You Should Use a Virtual Environment in Python](https://techisnotmagic.blogspot.com/2025/02/why-you-should-use-virtual-environment.html)

    Step 4: Install Dependencies
    Now that your virtual environment is active, install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
    Step 5: Run the Flask application
    ```bash
    flask --app server run
    ```
No matter which option, the application should now be accessible at http://127.0.0.1:5000 in you local machine.

## License
MIT License

## Contact
If you have any questions, feel free to ask me.

## Acknowledgments
- This mini-project was inspired by the final project training in IBM [Developing AI Applications with Python and Flask](https://www.coursera.org/learn/python-project-for-ai-application-development)

- I use the following model in my project: 
**Jochen Hartmann**. (2022). *Emotion English DistilRoBERTa-base*. [Hugging Face Model](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/)
