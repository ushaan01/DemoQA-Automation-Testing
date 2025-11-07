🖥️ DemoQA Selenium Automation Project


📖 Overview

This is a Python Selenium automation project for DemoQA that demonstrates:

1) Browser automation with Selenium

2) Test organization using PyTest

3) Page Object Model (POM) structure

4) Data-driven testing using Excel files

Automated sections:

1) Elements → Text Box

2) Forms → Practice Form

3) Widgets → Slide
   

📂 Project Structure 

DemoQA-

│

├─ test_data/                  📄 Excel test data

│   └─ test_data.xlsx 

│

├─ pages/                      🏷️ Page Object Models

│   ├─ elements_page.py        # Text Box

│   ├─ forms_page.py           # Form

│   └─ widgets_page.py         # Slider

│

├─ test_cases/                 🧪 Test scripts

│   ├─ test_elements_page.py

│   ├─ test_forms_page.py

│   └─ test_widgets_page.py

│

├─ utilities/                  ⚙️ Helper functions

│   └─ read_excel.py   

│

├─ conftest.py                 🔧 PyTest setup

└─ README.md                   📝 Documentation


📝 Test Data

 Stored in test_data/test_data.xlsx


✏️ Elements

| full_name | email | current_address | permanent_address |

🗂️ Forms

| first_name | last_name | email | mobile |

🎚️ Slider

| offset |
