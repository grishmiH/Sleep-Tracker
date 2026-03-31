import csv
import os
from datetime import datetime, timedelta

FILE_NAME = "sleep_data.csv"

def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Hours Slept", "Quality (1-10)", "Notes"])
        print(f"Created new sleep log: {FILE_NAME}\n")

def log_sleep():
    """Log a new sleep entry."""
    print("--- Log Sleep ---")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    try:
        hours = float(input("Hours slept: "))
        quality = int(input("Sleep quality (1-10): "))
        if not (1 <= quality <= 10):
            print("Quality must be between 1 and 10.")
            return
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    notes = input("Any notes? (optional, press Enter to skip): ").strip()

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, hours, quality, notes])

    print(f" Sleep logged for {date}: {hours} hrs, Quality: {quality}/10")

def read_data():
    """Read all sleep data from CSV."""
    data = []
    if not os.path.exists(FILE_NAME):
        return data
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def view_all_logs():
    """Display all sleep logs."""
    data = read_data()
    if not data:
        print("No sleep data found. Start logging first!")
        return

    print("--- All Sleep Logs ---")
    print(f"{'Date':<15} {'Hours':<10} {'Quality':<10} {'Notes'}")
    print("-" * 55)
    for row in data:
        print(f"{row['Date']:<15} {row['Hours Slept']:<10} {row['Quality (1-10)']:<10} {row['Notes']}")

def weekly_report():
    """Generate a weekly sleep quality report for the last 7 days."""
    data = read_data()
    if not data:
        print("No data available for a report.")
        return

    today = datetime.today().date()
    week_ago = today - timedelta(days=7)

    weekly_data = []
    for row in data:
        try:
            row_date = datetime.strptime(row['Date'], "%Y-%m-%d").date()
            if week_ago <= row_date <= today:
                weekly_data.append(row)
        except ValueError:
            continue

    if not weekly_data:
        print("\nNo data found for the last 7 days.")
        return

    hours_list = [float(row['Hours Slept']) for row in weekly_data]
    quality_list = [int(row['Quality (1-10)']) for row in weekly_data]

    avg_hours = sum(hours_list) / len(hours_list)
    avg_quality = sum(quality_list) / len(quality_list)
    best_day = weekly_data[hours_list.index(max(hours_list))]
    worst_day = weekly_data[hours_list.index(min(hours_list))]

    print("--- Weekly Sleep Report (Last 7 Days) ---")
    print(f"Days Logged     : {len(weekly_data)}")
    print(f"Average Sleep   : {avg_hours:.1f} hours/night")
    print(f"Average Quality : {avg_quality:.1f}/10")
    print(f"Best Night      : {best_day['Date']} ({best_day['Hours Slept']} hrs)")
    print(f"Worst Night     : {worst_day['Date']} ({worst_day['Hours Slept']} hrs)")

    print(" Health Tip:")
    if avg_hours < 6:
        print("   You're sleeping too little. Aim for at least 7-8 hours per night.")
    elif avg_hours < 7:
        print("   You're slightly below the recommended 7-8 hours. Try sleeping 30 mins earlier.")
    elif avg_hours <= 9:
        print("   Great job! You're within the healthy sleep range. Keep it up!")
    else:
        print("   You're sleeping more than 9 hours. Check if you feel rested — oversleeping can also affect health.")

def main():
    initialize_file()
    print("=" * 40)
    print("  Sleep Tracker - Stay Rested!")
    print("=" * 40)

    while True:
        print("What would you like to do?")
        print("1. Log tonight's sleep")
        print("2. View all logs")
        print("3. Weekly sleep report")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == '1':
            log_sleep()
        elif choice == '2':
            view_all_logs()
        elif choice == '3':
            weekly_report()
        elif choice == '4':
            print("Goodnight! Sleep well.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
