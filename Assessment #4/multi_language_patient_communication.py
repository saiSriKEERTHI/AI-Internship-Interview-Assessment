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
        "Tamil": "\u0B89\u0B99\u0BCD\u0B95\u0BB3\u0BCD \u0BA8\u0BC7\u0BB0\u0BAE\u0BCD \u0B89\u0BB1\u0BC1\u0BA4\u0BBF\u0B9A\u0BC6\u0BAF\u0BCD\u0BAF\u0BAA\u0BCD\u0BAA\u0B9F\u0BBF\u0BB1\u0BCD\u0BB1\u0BCB\u0BAE\u0BCD. \u0BA4\u0BAF\u0BB5\u0BC1\u0B9A\u0BC6\u0BAF\u0BCD\u0BA4\u0BC1 \u0BB5\u0BB0\u0BC1\u0B95!",
        "Telugu": "\u0C2E\u0C40 \u0C28\u0C3F\u0C2F\u0C3E\u0C2E\u0C15\u0C02 \u0C28\u0C3F\u0C30\u0C4D\u0C27\u0C3E\u0C30\u0C3F\u0C02\u0C1A\u0C2C\u0C21\u0C3F\u0C02\u0C26\u0C3F. \u0C26\u0C2F\u0C1A\u0C47\u0C38\u0C3F \u0C30\u0C02\u0C21\u0C3F!",
        "Malayalam": "\u0D28\u0D3F\u0D19\u0D4D\u0D19\u0D33\u0D41\u0D1F\u0D46 \u0D05\u0D2A\u0D4B\u0D2F\u0D3F\u0D28\u0D4D\u0D1F\u0D4D\u0D2E\u0D46\u0D23\u0D4D\u0D1F\u0D4D \u0D38\u0D26\u0D3F\u0D15\u0D4D\u0D15\u0D3F\u0D30\u0D3F\u0D15\u0D4D\u0D15\u0D3F\u0D30\u0D3F\u0D1A\u0D4D\u0D1A\u0D41. \u0D26\u0D2F\u0D35\u0D3E\u0D2F\u0D3F \u0D35\u0D30\u0D42!",
        "Hindi": "\u0906\u092A\u0915\u093E \u0905\u092A\u0949\u092F\u0902\u091F\u092E\u0947\u0902\u091F \u0915\u0928\u094D\u092B\u0930\u094D\u092E \u0939\u094B \u0917\u092F\u093E \u0939\u0948\u0964 \u0915\u0943\u092A\u092F\u093E \u0906\u090F\u0902!",
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
        print(f"\U0001F4E9 Sending {message_type} via {channel} to {patient['name']} ({language}): {message}")

def convert_text_to_speech(text, language, patient_name):
    """Convert text to speech for IVR"""
    lang_code = {"Tamil": "ta", "Telugu": "te", "Malayalam": "ml", "Hindi": "hi", "English": "en"}
    
    # Get correct language code for TTS (default to English)
    lang = lang_code.get(language, "en")
    
    filename = f"{patient_name.replace(' ', '_')}_ivr_message.mp3"  # Replace spaces with underscores
    
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)
        print(f"✅ File saved: {filename}")
        
        if os.path.exists(filename):
            os.system(f"start {filename}")  # Play file on Windows
            print(f"🔊 Playing IVR message for {patient_name} in {language}")
        else:
            print(f"❌ Error: File {filename} was not created!")
    except Exception as e:
        print(f"⚠️ Error generating speech: {e}")

# Simulating message sending for all patients
for patient in patients:
    send_message(patient, "Appointment Confirmation")

