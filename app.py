import os
from flask import Flask, request, send_file, jsonify, render_template
from PyPDF2 import PdfReader, PdfWriter
from itertools import product
import string
import threading

app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = "uploads"
UNLOCKED_FOLDER = "unlocked"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(UNLOCKED_FOLDER, exist_ok=True)

brute_thread = None
pause_flag = threading.Event()
stop_flag = threading.Event()
found_password = ""
current_try = ""
pdf_path = ""
unlocked_pdf_path = ""

def get_charset(charset_option):
    if charset_option == "upper":
        return string.ascii_uppercase
    elif charset_option == "lower":
        return string.ascii_lowercase
    else:
        return string.ascii_letters  # mixed

def brute_force_pdf(pdf_file_path, length, charset_option):
    global found_password, current_try, unlocked_pdf_path
    charset = get_charset(charset_option)

    try:
        for l in range(1, length + 1):
            for combo in product(charset, repeat=l):
                if stop_flag.is_set():
                    return
                while pause_flag.is_set():
                    pause_flag.wait()

                current_try = ''.join(combo)

                reader = PdfReader(pdf_file_path)
                if reader.decrypt(current_try):
                    writer = PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)

                    unlocked_pdf_path = os.path.join(UNLOCKED_FOLDER, "unlocked.pdf")
                    with open(unlocked_pdf_path, "wb") as f:
                        writer.write(f)

                    found_password = current_try
                    return
    except Exception as e:
        print("Error:", e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    global brute_thread, found_password, current_try, pdf_path, unlocked_pdf_path
    stop_flag.clear()
    pause_flag.clear()
    found_password = ""
    current_try = ""
    unlocked_pdf_path = ""

    file = request.files["file"]
    length = int(request.form["length"])
    charset = request.form["charset"]
    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    brute_thread = threading.Thread(target=brute_force_pdf, args=(pdf_path, length, charset))
    brute_thread.start()
    return "Started"

@app.route("/pause")
def pause():
    pause_flag.set()
    return "Paused"

@app.route("/resume")
def resume():
    pause_flag.clear()
    return "Resumed"

@app.route("/stop")
def stop():
    stop_flag.set()
    return "Stopped"

@app.route("/status")
def status():
    return jsonify({
        "current_try": current_try,
        "found_password": found_password,
        "unlocked": bool(unlocked_pdf_path)
    })

@app.route("/download")
def download():
    if unlocked_pdf_path and os.path.exists(unlocked_pdf_path):
        return send_file(unlocked_pdf_path, as_attachment=True)
    return "No unlocked file found", 404

if __name__ == "__main__":
    app.run(debug=True)
