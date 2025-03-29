# Assessment 2

# Scenario-Based Assessment

# Problem Statement:
    "Schedula needs to implement an Intelligent Queue Management system for a medical practice with the following characteristics:

* 50 doctors with varied scheduling patterns
* Each doctor sees 30-50 patients daily in 3-hour blocks
* Patients arrive unpredictably, often not at their scheduled times
* Appointments come from multiple channels (IVR, app, WhatsApp)
* Walk-in patients need to be accommodated
* Some doctors track patient status (arrived, waiting, consulted), but not all"

# Task Requirements:

1. Break down this problem into logical components and steps (no technical knowledge required)
2. Identify what information would be necessary to make intelligent queuing decisions
3. Describe how you would measure if your queue management system is working effectively
4. Explain how the system should handle communication with patients about wait times
5. Record a 3-minute Loom video explaining your approach


# Expected Solution Format

1. Problem Breakdown

Logical Components & Steps
- Doctor Schedules & Availability:

    Track individual doctor schedules and real-time availability.

- Patient Arrival & Appointment Handling:

    Consider scheduled vs. actual arrival times.

    Handle walk-ins and reschedule missed appointments.

- Multi-Channel Appointment Sources:

    Integrate IVR, app, WhatsApp, and walk-in bookings into a central system.

- Queue Optimization & Prioritization:

    Assign patients dynamically based on real-time queue length, urgency, and doctor availability.

- Patient Status Tracking:

    Implement real-time updates for "arrived," "waiting," and "consulted" statuses.

2. Required Information for Intelligent Queuing
- Doctor’s live schedule & consultation durations.

- Real-time patient check-in & arrival patterns.

- Historical appointment data to predict peak loads.

- Channel-wise booking trends (app, IVR, walk-ins).

- Doctor-specific queue preferences (e.g., some prefer walk-ins, others don’t).

3. Measuring System Effectiveness
- Average Wait Time Reduction: Compare before vs. after implementation.

- Queue Efficiency Score: Patients served per doctor per time block.

- Patient Satisfaction Metrics: Collect feedback via app/SMS.

- No-show & Walk-in Handling: Track how well system accommodates unexpected arrivals.

4. Patient Communication Strategy
- Real-time ETA Updates: SMS/App notifications for estimated wait time.

- Rescheduling Option: If wait time exceeds X minutes, suggest alternatives.

- Check-in Confirmation: Automated message when the doctor is ready.


## Instructions:
1. Clone this repository.
3. Raise a Pull Request (PR) with your solution.
4. Record a video explaining your solution.
5. Attach the video link in the submission form.
6. Submit the PR link in the submission form.