# pomodoro.py
import time
from datetime import datetime
import database
import notifications

class PomodoroTimer:
    def __init__(self, work_minutes=25, break_minutes=5):
        self.work_time = work_minutes * 60
        self.break_time = break_minutes * 60

    def start_work_session(self, project_name):
        """Start a 25-minute work session."""
        notifications.send("FocusLog", f"Work started: {project_name}")
        print(f"✅ Work session started: {project_name} ({self.work_time // 60} min)")

        start_time = datetime.now()
        time.sleep(self.work_time)  # In GUI version, replace with real countdown
        end_time = datetime.now()

        database.add_session(project_name, start_time, end_time)

        notifications.send("FocusLog", "Work finished! Time for a break 🍵")
        print("✅ Work completed. Starting break...")

    def start_break_session(self):
        """Start a 5-minute break."""
        print(f"☕ Break started: {self.break_time // 60} minutes")
        time.sleep(self.break_time)
        notifications.send("FocusLog", "Break ended! Ready to go again 💪")