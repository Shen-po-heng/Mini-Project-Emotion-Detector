"""
Flask web server for emotion detection using the EmotionDetection package.
Author: Po-Heng
"""

from flask import Flask, render_template, request
from src.emotiondetection.emotion_detection import emotion_detector
import os

# Get the project root directory
project_root = os.path.abspath(os.path.dirname(__file__))
print(f"Project root directory: {project_root}")
# Specify the paths for templates and static folders
templates_path = os.path.join(project_root, 'src', 'templates')
print(f"Template folder path: {templates_path}")

static_path = os.path.join(project_root, 'src', 'static')

app = Flask(
    "emotion_detector", 
    template_folder=templates_path,  # Correct path for templates
    static_folder=static_path
)

@app.route("/emotionDetector", methods=['GET', 'POST'])
def sent_analyzer():
    """
    Analyze the sentiment of the given text.

    Returns:
        str: Emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is {response}"

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        HTML: The rendered index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
