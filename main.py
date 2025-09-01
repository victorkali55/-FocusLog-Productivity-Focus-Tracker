# main.py
import pomodoro
import database
import report
import notifications
from datetime import datetime

def clear_screen():
    print("\n" * 3)

def main():
    database.create_tables()
    timer = pomodoro.PomodoroTimer(work_minutes=1, break_minutes=1)  # For testing (use 25,5 in production)

    while True:
        clear_screen()
        print("🎯 FOCUSLOG – Focus & Productivity Tracker")
        print("1. Start Pomodoro Session")
        print("2. Show Weekly Chart")
        print("3. Export PDF Report")
        print("4. View Today's Total")
        print("5. Exit")
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            project = input("Project name: ").strip()
            if not project:
                project = "General Work"
            timer.start_work_session(project)
            timer.start_break_session()

        elif choice == "2":
            report.show_weekly_chart()

        elif choice == "3":
            import os
            if not os.path.exists("reports"):
                os.makedirs("reports")
            report.export_pdf_report()

        elif choice == "4":
            today = datetime.now().strftime("%Y-%m-%d")
            total = database.get_daily_total(today)
            hours = total / 60
            print(f"\n✅ Today: {total} minutes ({hours:.1f} hours)")
            input("Press Enter to continue...")

        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")
            input("Press Enter to try again...")

if __name__ == "__main__":
    main()