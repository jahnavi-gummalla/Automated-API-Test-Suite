# Automated API Test Suite

This project demonstrates automated REST API testing using Python, Pytest, and Requests.

## 🚀 Features
- Automated testing of REST APIs (GET, POST, PUT, DELETE)
- Uses Pytest for test execution
- Generates HTML test reports using pytest-html
- Clean and simple test structure

## 🛠️ Tech Stack
- Python
- Pytest
- Requests
- pytest-html

## 📂 Project Structure
Automated-API-Test-Suite/
│── tests/
│   ├── test_api.py
│   ├── conftest.py
│
│── requirements.txt
│── README.md

## ⚙️ Setup Instructions

1. Clone the repository:
git clone https://github.com/jahnavi-gummalla/Automated-API-Test-Suite.git

2. Navigate into the folder:
cd Automated-API-Test-Suite

3. Install dependencies:
pip install -r requirements.txt

## ▶️ Run Tests

pytest

## 📊 Generate HTML Report

pytest --html=reports/report.html

## 📌 Notes
- Uses public APIs (JSONPlaceholder / ReqRes)
- Can be extended with authentication and CI/CD

## 👩‍💻 Author
Jahnavi Gummalla
