import torch
from transformers import pipeline

# Initialize the Hugging Face pipeline for emotion detection
emotion_classifier = pipeline("text-classification", 
                                model="j-hartmann/emotion-english-distilroberta-base", 
                                top_k=5)

def emotion_detector(text_to_analyze):
    # Use the model to predict emotions
    result = emotion_classifier(text_to_analyze)

    if result:
        # Get the most probable emotion
        emotions = {item['label']: item['score'] for item in result[0]}

        dominant_emotion = max(emotions, key=emotions.get)
        emotion_score = emotions[dominant_emotion]
        other_emotions = {emotion: score for emotion, score in emotions.items() if emotion != dominant_emotion}

        return {
            'dominant_emotion': dominant_emotion,
            'emotion_score': emotion_score,
            'other_emotions': other_emotions
        }
    else:
        return None

if __name__ == '__main__':
    text="I am glad this happened"
    result = emotion_detector(text)
    print(result)
