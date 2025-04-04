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
        "Tamil": "உங்கள் நியமனம் உறுதியாக உள்ளது. தயவுசெய்து வருக!",
        "Telugu": "మీ అపాయింట్‌మెంట్ నిర్ధారించబడింది. దయచేసి రండి!",
        "Malayalam": "നിങ്ങളുടെ അപ്പോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചു. ദയവായി വരൂ!",
        "Hindi": "आपकी नियुक्ति की पुष्टि हो गई है। कृपया आएं!",
        "English": "Your appointment is confirmed. Please visit!"
    }
}

def send_message(patient, message_type):
    """Send a message based on patient language and preferred channel"""
    language = patient["language"]
    channel = patient["channel"]
    
    # Get the correct message type (default to English if language not found)
    message = messages.get(message_type, {}).get(language, messages["Appointment Confirmation"]["English"])
    
    if channel == "IVR":
        # Convert text message to speech for IVR call
        convert_text_to_speech(message, language, patient["name"])
    else:
        print(f"📩 Sending '{message_type}' via {channel} to {patient['name']} ({language}):\n   📝 {message}\n")

def convert_text_to_speech(text, language, patient_name):
    """Convert text to speech for IVR"""
    lang_code = {"Tamil": "ta", "Telugu": "te", "Malayalam": "ml", "Hindi": "hi", "English": "en"}
    
    # Get correct language code for TTS (default to English)
    lang = lang_code.get(language, "en")
    
    filename = f"{patient_name.replace(' ', '_')}_ivr_message.mp3"  # Replace spaces with underscores
    
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)
        print(f"✅ IVR File saved: {filename}")
        
        if os.path.exists(filename):
            os.system(f"start {filename}")  # Play file on Windows
            print(f"🔊 Playing IVR message for {patient_name} in {language}\n")
        else:
            print(f"❌ Error: File {filename} was not created!\n")
    except Exception as e:
        print(f"⚠️ Error generating speech: {e}\n")

# Simulating message sending for all patients
for patient in patients:
    send_message(patient, "Appointment Confirmation")


