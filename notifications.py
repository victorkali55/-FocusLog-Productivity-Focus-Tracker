# notifications.py
from plyer import notification

def send(title, message):
    """Send desktop notification."""
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )