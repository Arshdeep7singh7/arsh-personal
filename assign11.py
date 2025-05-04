import cv2
import pytesseract
import re
import pyttsx3

# Set Tesseract path (adjust based on your OS)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # MacOS example

def read_label(image_path):
    # Load image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # OCR processing
    text = pytesseract.image_to_string(gray)
    
    # Extract critical info using regex
    dosage = re.search(r'\d+\s*mg', text)
    frequency = re.search(r'take\s*\d+\s*times daily', text, re.IGNORECASE)
    
    # Vocalize instructions
    engine = pyttsx3.init()
    if dosage and frequency:
        instruction = f"Take {dosage.group()} {frequency.group()}."
    else:
        instruction = "Warning: Could not read dosage. Consult a pharmacist."
    
    engine.say(instruction)
    engine.runAndWait()

# Example usage
read_label("medicine_label.jpg")
import cv2
import numpy as np
from keras.models import load_model

# Load pre-trained emotion model (e.g., FER-2013)
emotion_model = load_model('fer2013_model.h5')  # Replace with your model path
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def detect_emotion():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to grayscale and detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            roi = cv2.resize(roi, (48, 48))
            roi = roi.astype('float') / 255.0
            roi = np.expand_dims(roi, axis=0)
            
            # Predict emotion
            prediction = emotion_model.predict(roi)[0]
            emotion = emotion_labels[np.argmax(prediction)]
            
            # Display emotion
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            # Adaptive feedback based on emotion
            if emotion in ['Angry', 'Fear', 'Sad']:
                print("[System] You seem stressed. Let me repeat the instructions slowly.")
        
        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Run emotion detection
detect_emotion()
import threading

# Run label reader and emotion detection in parallel
def run_system():
    label_thread = threading.Thread(target=read_label, args=("medicine_label.jpg",))
    emotion_thread = threading.Thread(target=detect_emotion)
    
    label_thread.start()
    emotion_thread.start()
    
    label_thread.join()
    emotion_thread.join()

if __name__ == "__main__":
    run_system()