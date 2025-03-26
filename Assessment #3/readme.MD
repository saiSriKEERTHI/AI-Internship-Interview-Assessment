# Assessment 3

# App-Based Simulation Tasks

# Problem Outline:

* Dynamic Scheduling Challenge
Mock Scenario: Candidates interact with a simplified Schedula admin interface showing:

Doctor Dashboard Simulation:
┌────────────────────────────┐
│ Dr. Smith - Cardiology     │
│ Available: 5PM-8PM (3 hrs) │
│ Appointments:              │
│ 5:00 PM - R. Patel         │
│ 5:15 PM - A. Kumar         │
│ 5:30 PM - **[Delay Alert]**│
│ 5:45 PM - M. Iyer          │
│ 6:00 PM - **[Walk-In]**    │
└────────────────────────────┘

* Questions:
A. Identify 3 key variables affecting schedule integrity
B. Propose AI-enhanced adjustments to maintain patient flow
* Multi-Channel Integration Puzzle
Data Visualization Task:

Appointment Sources (Simulated Data):
IVR       | App      | WhatsApp  
╠═══════╦════════╦═════════╣
72%      | 18%     | 10%     

No-Show Rates by Channel:
IVR: 35% | App: 12% | WhatsApp: 18%

* Challenge: Design an AI solution that improves adherence across channels


# Expected Solution Format

1. Key Variables Affecting Schedule Integrity
- Appointment Delays: Some consultations may take longer than expected, causing cascading delays.

- Walk-Ins & No-Shows: Unexpected patient arrivals and last-minute cancellations disrupt the schedule.

- Multi-Channel Booking Variability: Different appointment sources (IVR, app, WhatsApp) have varying no-show rates, impacting efficiency.

2. AI-Enhanced Adjustments for Patient Flow
- Predictive Delay Management: Use historical data to predict consultation durations and adjust upcoming slots dynamically.

- Smart Rescheduling: If a delay is detected, suggest real-time slot reassignments to optimize doctor availability.

- AI-Powered Patient Communication: Send automated updates via app/SMS for estimated wait times and reschedule options.

3. AI Solution for Multi-Channel Booking Adherence
- No-Show Risk Prediction: Identify high-risk no-show appointments and send reminders or auto-adjustments.

- Channel-Based Booking Allocation: Adjust appointment quotas based on the reliability of each channel.

- Incentivized Confirmation System: Encourage confirmations from IVR users via SMS reminders or small incentives.

4. Measuring Success
- Reduction in Average Wait Times: Track improvements in real-time scheduling.

- No-Show Rate Reduction: Compare no-show rates before and after implementing AI optimizations.

- Patient Satisfaction Scores: Collect feedback via automated surveys.


## Instructions:
1. Clone this repository.
3. Raise a Pull Request (PR) with your solution.
4. Record a video explaining your solution.
5. Attach the video link in the submission form.
6. Submit the PR link in the submission form.