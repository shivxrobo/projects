import time
from datetime import datetime
from plyer import notification
import schedule

def notify_task():
    task_description = "Remember to do your task!"
    notification.notify(
        title='Task Reminder',
        message=task_description,
        app_name='Task Reminder App',
        timeout=10
    )

def schedule_daily_reminder(task_time):
    # Convert the task time string to a datetime object
    task_datetime = datetime.strptime(task_time, '%H:%M')

    # Schedule the daily reminder
    schedule.every().day.at(task_datetime.strftime('%H:%M')).do(notify_task)

    # Keep the script running to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Set the time for the daily reminder in 24-hour format (e.g., "18:30")
    task_time = "12:00"

    # Start scheduling the daily reminder
    schedule_daily_reminder(task_time)