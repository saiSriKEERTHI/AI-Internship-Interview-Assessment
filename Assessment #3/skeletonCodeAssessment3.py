import random
from datetime import datetime, timedelta

class DoctorSchedule:
    def __init__(self, doctor_name, available_from, available_to):
        self.doctor_name = doctor_name
        self.available_from = available_from
        self.available_to = available_to
        self.appointments = []
    
    def add_appointment(self, time, patient_name, source):
        self.appointments.append({
            "time": time, 
            "patient": patient_name, 
            "source": source,
            "status": "Scheduled",
            "predicted_delay": self.predict_delay()
        })

    def predict_delay(self):
        """AI model can enhance this prediction based on real data."""
        return random.choice([0, 5, 10, 15])  # Simulating random delays

    def optimize_schedule(self):
        """Dynamically adjust schedule based on predicted delays"""
        for i in range(len(self.appointments) - 1):
            if self.appointments[i]["predicted_delay"] > 0:
                self.appointments[i+1]["time"] += timedelta(minutes=self.appointments[i]["predicted_delay"])

    def display_schedule(self):
        print(f"Doctor {self.doctor_name} ({self.available_from} - {self.available_to})")
        for appt in self.appointments:
            delay = f"[Delay: {appt['predicted_delay']} min]" if appt["predicted_delay"] > 0 else ""
            print(f"  {appt['time']} - {appt['patient']} ({appt['source']}) {delay}")

# Example Usage
schedule = DoctorSchedule("Dr. Smith", "5:00 PM", "8:00 PM")

schedule.add_appointment(datetime(2025, 3, 26, 17, 0), "R. Patel", "App")
schedule.add_appointment(datetime(2025, 3, 26, 17, 15), "A. Kumar", "IVR")
schedule.add_appointment(datetime(2025, 3, 26, 17, 30), "[Walk-In]", "Walk-In")

schedule.optimize_schedule()
schedule.display_schedule()
