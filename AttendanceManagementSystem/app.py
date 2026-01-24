from flask import Flask
from controllers.attendanceController import attendance_bp
from models.attendanceModel import create_table

app = Flask(__name__)
app.register_blueprint(attendance_bp)

create_table()  # Ensure table exists

if __name__ == "__main__":
    app.run(debug=True)

