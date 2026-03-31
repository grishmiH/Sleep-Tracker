# Sleep-Tracker

Sleep Tracker — CLI-Based Sleep Logger & Weekly Report Generator

A beginner-friendly Python command-line application that helps you log your nightly sleep and generate a weekly sleep quality report. Built as a capstone project for the Python Essentials course.


Problem Statement

Many students and working individuals neglect tracking their sleep, which leads to poor health, low productivity, and fatigue. Most sleep-tracking apps are complex or require expensive devices. This tool offers a simple, no-internet, no-app-required solution using just Python and a CSV file.

Features
 Log each night's sleep — date, hours slept, quality rating (1–10), and optional notes
 View all past sleep logs in a clean table
 Generate a weekly report — average sleep, best night, worst night
 Get a personalized health tip based on your average sleep hours
 Data is saved in a local CSV file and persists across sessions

Technologies Used
Python 3.x
Built-in libraries only: `csv`, `os`, `datetime`
No external dependencies required



How to Use

When you run the program, you will see a menu:

========================================

Sleep Tracker - Stay Rested!

What would you like to do?

Log tonight's sleep

View all logs

Weekly sleep report

Exit


Option 1 — Log Sleep

Enter the date (or press Enter for today), hours slept, quality rating (1–10), and an optional note.

Option 2 — View All Logs

Displays all previously logged entries in a table format.

Option 3 — Weekly Report

Shows your sleep stats for the last 7 days:

Number of days logged

Average hours and quality

Best and worst night

A personalized health tip

Option 4 — Exit

Exits the program.



-Project Structure

sleep-tracker/

│
├── sleep_tracker.py        # Main Python application

├── sleep_data.csv          # Auto-created when you first log sleep

└── README.md               # Project documentation


-Sample Output

--- Weekly Sleep Report (Last 7 Days) ---

Days Logged     : 5

Average Sleep   : 6.8 hours/night

Average Quality : 7.2/10

Best Night      : 2026-03-28 (8.5 hrs)

Worst Night     : 2026-03-26 (5.0 hrs)

Health Tip:

You're slightly below the recommended 7-8 hours. Try sleeping 30 mins earlier.




-My Details
Name: Grishmi Halai
Course: Python Essentials
University: VIT Bhopal University
