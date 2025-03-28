import random
from gtts import gTTS
import os

# Sample patient database with language and preferred communication channel
patients = [
    {"id": 1, "name": "Ravi Kumar", "language": "Tamil", "channel": "SMS"},
    {"id": 2, "name": "Ananya Rao", "language": "Telugu", "channel": "WhatsApp"},
    {"id": 3, "name": "Joseph Mathew", "language": "Malayalam", "channel": "IVR"},  # IVR (Voice Call)
    {"id": 4, "name": "Rahul Sharma", "language": "Hindi", "channel": "SMS"},
    {"id": 5, "name": "David Thomas", "language": "English", "channel": "WhatsApp"},
]

# Predefined multi-language messages for different notifications
messages = {
    "Appointment Confirmation": {
        "Tamil": "உங்கள் நேரம் உறுதிசெய்யப்பட்டது. தயவுசெய்து வருக!",
        "Telugu": "మీ నియామకం నిర్ధారించబడింది. దయచేసి రండి!",
        "Malayalam": "നിങ്ങളുടെ അപോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചിരിക്കുന്നു. ദയവായി വരൂ!",
        "Hindi": "आपका अपॉइंटमेंट कन्फर्म हो गया है। कृपया आएं!",
        "English": "Your appointment is confirmed. Please visit!"
    }
}

def send_message(patient, message_type):
    """Send a message based on patient language and preferred channel"""
    language = patient["language"]
    channel = patient["channel"]
    
    # Get the correct message type (default to English if language not found)
    message = messages[message_type].get(language, messages[message_type]["English"])
    
    if channel == "IVR":
        # Convert text message to speech for IVR call
        convert_text_to_speech(message, language, patient["name"])
    else:
        print(f"📩 Sending {message_type} via {channel} to {patient['name']} ({language}): {message}")

def convert_text_to_speech(text, language, patient_name):
    """Convert text to speech for IVR"""
    lang_code = {"Tamil": "ta", "Telugu": "te", "Malayalam": "ml", "Hindi": "hi", "English": "en"}
    
    # Get correct language code for TTS (default to English)
    lang = lang_code.get(language, "en")
    
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = f"{patient_name}_ivr_message.mp3"
    
    # Save and play voice message
    tts.save(filename)
    os.system(f"start {filename}")  # For Windows
    print(f"🔊 Playing IVR message for {patient_name} in {language}")

# Simulating message sending for all patients
for patient in patients:
    send_message(patient, "Appointment Confirmation")

