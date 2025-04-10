# TalentScout Hiring Assistant

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

##  Project Overview

TalentScout is an AI-powered hiring assistant designed to streamline the candidate screening process. It gathers essential candidate details and uses a large language model (LLM) to generate tailored technical interview questions based on the candidate's declared tech stack.

Built with Python and Streamlit, this application demonstrates the effective use of:
- Prompt engineering
- Session-based routing
- Custom UI navigation

---

##  Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sashank-Sagar/TalentScout-Chatbot.git
cd TalentScout-Chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv env
```

### 3. Activate the Virtual Environment
**On Windows:**
```bash
env\Scripts\activate
```
**On PowerShell:**
```bash
env\Scripts\Activate.ps1
```
**On macOS/Linux:**
```bash
source env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
streamlit run app.py
```

---

##  Usage Guide

### 🔹 Navigation
Use the custom sidebar navigation to switch between:
- **Home**: Project overview and instructions
- **Candidate Form**: Enter candidate details (name, email, phone, experience, position, location, tech stack)
- **Interview Questions**: Generate and download tailored questions

### 🔹 Candidate Form
Fill in all required fields. Submitted data is stored in Streamlit's session state for use across pages.

### 🔹 Interview Questions
The app uses LLM prompts to generate multiple technical questions per selected technology. These are displayed on-screen and can be downloaded.

---

##  Technical Details

###  Architecture & Code Structure
```
TalentScout-Chatbot/
├── app.py                  # Main script with page routing
├── helper_functions.py     # Custom sidebar rendering logic
├── CB_logic.py             # Core chatbot logic for question generation
├── prompts.py              # Prompt templates
├── views/                  # Page components
│   ├── candidate_form.py   # Candidate form input page
│   └── interview_ques.py   # Technical questions output page
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

###  Design Highlights
- **Session-based Routing**: Replaces Streamlit's default multipage layout with dynamic control using `st.session_state`
- **Custom Sidebar**: Vertical navigation buttons with `st.rerun()` logic
- **Prompt Engineering**:
  - **Candidate Info Prompt**: Extracts relevant, clean information
  - **Tech Stack Prompt**: Asks for 5 well-formed, difficulty-balanced questions per tech
- **Input Validation**: Ensures valid and complete inputs (email, phone, etc.)

###  Prompt Strategy
- Clearly instructs the LLM for concise, skill-relevant questions
- Balanced difficulty to simulate real interviews
- One prompt per tech stack element, dynamically iterated

---

##  Challenges & Solutions

| Challenge                | Solution                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| API Rate Limits          | Added caching using `st.session_state` and simple error handling         |
| Navigation Jumps         | Resolved using button states and `st.rerun()` logic                      |
| UI Consistency           | Custom sidebar and minimal layout for clean UX                          |
| Data Consistency         | Used session memory to keep candidate data across pages                  |

---

##  Data Privacy
- **Simulated Data**: Candidate data is anonymized in the demo
- **No Storage**: No backend database or persistent logging
- **GDPR-Friendly**: Designed for privacy-first use

---

##  Author
- **Sashank Sagar**
  - [GitHub](https://github.com/Sashank-Sagar)
  - [LinkedIn](https://linkedin.com/in/sashank-sagar)

---

##  License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full license details.

---

##  Contributions
If you'd like to contribute, feel free to fork the repo and open a pull request.  
Suggestions, issues, or feature ideas are welcome in the [Issues](https://github.com/Sashank-Sagar/TalentScout-Chatbot/issues) tab!

