# 🧪 TDD Anagram Detector (Python + Jupyter)

This project demonstrates the use of **Test-Driven Development (TDD)** in Python to build an **Anagram Detector**. All development was done using **Jupyter Notebook**, with code exported into Python modules and tested using the built-in `unittest` framework.

CI/CD is configured using **GitHub Actions**, which automatically runs all test cases on every push to the `main` branch.

---

## 📌 Problem Statement

An anagram is a word or phrase formed by rearranging the letters of another, ignoring case and spaces.

### Examples:
- `"listen"` and `"silent"` → ✅ Anagram  
- `"conversation"` and `"voices rant on"` → ✅ Anagram  
- `"hello"` and `"world"` → ❌ Not an anagram

---

## ⚙️ Features

- Follows **Red-Green-Refactor** cycle of TDD
- Handles:
  - Case insensitivity
  - Whitespace
- Fully tested using `unittest`
- CI via **GitHub Actions**

---

## 📂 Project Structure


dd-anagram-detector/
│
├── anagram_detector.ipynb     # Jupyter Notebook showing full TDD process
├── anagram.py                 # Main function logic
├── test_anagram.py            # Unit tests using unittest
│
└── .github/
└── workflows/
└── python-app.yml     # GitHub Actions workflow file


---

## 🧪 Run Tests Locally

Inside Jupyter Notebook or Python:

```python
import unittest
unittest.main(argv=[''], verbosity=2, exit=False)

python -m unittest discover -s . -p "test_*.py"



itHub Actions CI

✅ Automatically runs all unit tests on every push to main.
📍 CI file location: .github/workflows/python-app.yml

⸻

🧾 Deliverables
	•	✅ Source Code (.py files)
	•	✅ Jupyter Notebook (.ipynb)
	•	✅ GitHub Actions CI
	•	✅ Exported PDF for Turnitin
	•	✅ Loom Video (.mp4)
	•	✅ .zip of all files
	•	✅ Public GitHub Repo

⸻

👤 Author

Tobi Faulkner
Python | TDD | Data Science Apprentice
🔗 GitHub: tobubu-ops

⸻

📜 License

This project is for educational/demo purposes under fair use.
