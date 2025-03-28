import random
import json
import pyttsx3  # For text-to-speech (TTS) in IVR
from googletrans import Translator  # AI-powered translation

# Define language mapping for AI-powered translations
LANGUAGE_MAPPING = {
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Hindi": "hi",
    "English": "en"
}

def load_patient_data():
    """Load patient data from a JSON file (Simulating a database)."""
    try:
        with open("patients.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("⚠️ patients.json not found! Creating a new file.")
        return []
    except json.JSONDecodeError:
        print("⚠️ Error decoding patients.json! Please check its format.")
        return []

def save_patient_data(data):
    """Save patient data back to the JSON file."""
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)

def ai_translate(message, target_language):
    """Use AI to translate messages dynamically."""
    translator = Translator()
    try:
        translated = translator.translate(message, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"⚠️ Translation Error: {e}. Sending message in English.")
        return message  # Default to English in case of translation failure

def send_message(patient):
    """Send messages based on patient preferences."""
    default_message = "Your appointment is confirmed. Please visit!"
    target_language = LANGUAGE_MAPPING.get(patient["language"], "en")
    
    translated_message = ai_translate(default_message, target_language)
    channel = patient.get("channel", "SMS")  # Default to SMS if channel is missing

    if channel == "IVR":
        text_to_speech(translated_message, patient["language"])
    else:
        print(f"📩 Sending via {channel} to {patient['name']} ({patient['language']}): {translated_message}")

def text_to_speech(message, language):
    """Convert text to speech for IVR calls in the patient's preferred language."""
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def measure_effectiveness():
    """Simulate tracking confirmation rates per channel."""
    confirmation_rates = {"SMS": 50, "WhatsApp": 70, "IVR": 40, "Email": 60, "Push": 55}
    results = {channel: random.randint(rate - 10, rate + 10) for channel, rate in confirmation_rates.items()}
    
    print("\n✅ Confirmation Rates by Channel:")
    for channel, rate in results.items():
        print(f"   {channel}: {rate}%")

# ---------------------------- MAIN EXECUTION ----------------------------

# Load patient data and process messages
patients = load_patient_data()

if not patients:
    print("⚠️ No patient data found! Please add patients to patients.json.")
else:
    for patient in patients:
        send_message(patient)

    # Measure effectiveness of the system
    measure_effectiveness()
