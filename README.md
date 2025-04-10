# MyGit - A Simple Git Clone

## Project Overview

MyGit is a simplified version control system inspired by Git. Designed as a learning project, it supports core Git features such as repository initialization, staging, committing, viewing logs, and file difference comparison. It is implemented in Python using a modular and class-based architecture.

---

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sashank-Sagar/MyGit.git
cd MyGit
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

### 5. Run the CLI
```bash
python main.py <command>
```

---

## Features Implemented

- **init**: Initialize a new MyGit repository
- **add**: Stage files for commit
- **commit**: Save a snapshot of the staged files
- **log**: View the commit history
- **diff**: Compare working directory changes against the last commit


---

## Usage Guide

Use the following CLI commands inside the project directory:

```bash
python main.py init             # Initialize a repo
python main.py add <filename>  # Add file to staging
python main.py commit -m "msg" # Commit with message
python main.py log             # Show commit logs
python main.py diff            # Show differences
```

---

## Code Structure
```
MyGit/
├── core/
│   ├── repository.py       # Init and config logic
│   ├── index.py            # Staging logic
│   ├── commit.py           # Commit management
│   └── diff.py             # File diff logic
├── utils/
│   └── file_ops.py         # File read/write helpers
├── main.py                 # CLI handler
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## Development Notes

- **Modular Design**: Each command’s logic is encapsulated in separate classes.
- **Reusable Helpers**: File operations and path management are handled through utility functions.
- **No External Database**: All data is stored in a `.mygit` directory within the project.
- **Educational Purpose**: Focuses on clarity and learning rather than performance or full Git replication.

---

## Author
- Sashank Sagar  
  [GitHub](https://github.com/Sashank-Sagar)  
  [LinkedIn](https://linkedin.com/in/sashank-sagar)

---

## Contributions
Feel free to fork the repository, submit pull requests, or open issues to suggest improvements or report bugs.

