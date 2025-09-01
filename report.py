# report.py
import matplotlib.pyplot as plt
import database
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def show_weekly_chart():
    """Display a bar chart of weekly productivity."""
    today = datetime.now()
    days = []
    hours = []

    for i in range(6, -1, -1):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        days.append(date[-5:])  # DD-MM format
        total_min = database.get_daily_total(date)
        hours.append(round(total_min / 60, 1))  # Convert to hours

    plt.figure(figsize=(10, 5))
    plt.bar(days, hours, color='skyblue')
    plt.title("Weekly Focus Hours")
    plt.xlabel("Date")
    plt.ylabel("Hours")
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

def export_pdf_report():
    """Export weekly report as PDF."""
    c = canvas.Canvas("reports/weekly_report.pdf", pagesize=A4)
    width, height = A4

    c.setFont("Helvetica", 16)
    c.drawString(50, height - 50, "FocusLog – Weekly Productivity Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Generated on: {datetime.now().strftime('%d %B %Y')}")

    # Table header
    c.drawString(50, height - 110, "Daily Summary (Hours):")
    y_position = height - 130

    total_hours = 0
    for i in range(7):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        mins = database.get_daily_total(date)
        hrs = round(mins / 60, 1)
        total_hours += hrs
        c.drawString(70, y_position, f"{date}: {hrs} hours")
        y_position -= 20

    c.drawString(50, y_position - 20, f"Total this week: {round(total_hours, 1)} hours")
    c.save()
    print("📄 PDF report saved as 'reports/weekly_report.pdf'")