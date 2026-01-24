from flask import Flask, render_template, request, redirect
from services import attendanceService as service
from models.attendanceModel import create_table

app = Flask(__name__)
create_table()  # Make sure table exists

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        message = service.mark_attendance(name)
        return redirect("/")  # Refresh page
    records = service.list_attendance()
    return render_template("index.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)

