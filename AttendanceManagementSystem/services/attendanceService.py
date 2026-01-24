from models import attendanceModel as model
from datetime import datetime

def mark_attendance(name):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Present"
    model.add_attendance(name, date, status)
    return f"Attendance marked for {name} at {date}"

def list_attendance():
    return model.get_attendance()

