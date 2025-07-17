# 🔐 PDF Unlocker - Alphabet Brute Force Tool

A modern brute-force based PDF password unlocker using only alphabetic characters (uppercase, lowercase, or mixed).

---

## 🌟 Features

- Upload and unlock encrypted PDF files using brute force
- Choose character set: UPPERCASE / lowercase / Mixed
- Set password length
- Live display of the password being attempted
- Toggle between Pause and Resume
- Stop button resets the app (clears uploaded file and progress)
- Final password shown once found
- Download unlocked PDF (link grays out until unlocked)
- Built using Flask, HTML, CSS, and JavaScript

---

## 📦 How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/pdf-unlocker-alphabet-bruteforce.git
   cd pdf-unlocker-alphabet-bruteforce
2. Install dependencies:
   pip install flask PyPDF2
3. Run the app:
   python app.py
4. Open your browser and go to:
   http://localhost:5000

📝 Note
⏳ Longer the password, more time it takes to brute force it.
For example:
3-letter lowercase: ~ seconds
5-letter mixed: ⚠️ could take hours depending on system

🧪 Example Encrypted PDFs
Sample locked PDFs are provided in the samples/ folder for testing:
uppercase-locked.pdf – password is 4 uppercase letters
lowercase-locked.pdf – password is 4 lowercase letters
mixed-locked.pdf – password consists of mixed-case letters

📁 Project Structure
pdf-unlocker-alphabet-bruteforce/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── script.js
├── uploads/
├── unlocked/
├── samples/
│   ├── uppercase-locked.pdf
│   ├── lowercase-locked.pdf
│   └── mixed-locked.pdf
├── LICENSE
└── README.md


