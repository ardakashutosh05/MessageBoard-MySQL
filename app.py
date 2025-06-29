from flask import Flask, render_template, request, redirect
from db_config import get_connection

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if name and message:
            cursor.execute("INSERT INTO messages (name, message) VALUES (%s, %s)", (name, message))
            conn.commit()
        return redirect("/")

    cursor.execute("SELECT * FROM messages ORDER BY id DESC")
    messages = cursor.fetchall()
    conn.close()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
