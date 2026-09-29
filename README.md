# Python Project

A Python project that can be cloned from GitHub and run locally on Windows.

---

## 📋 Requirements

Before starting, make sure you have:

* Windows 10 or Windows 11
* Git
* Python 3.10 or later
* VS Code (recommended)

### Check Python

Open **PowerShell** or **Git Bash**:

```bash
python --version
```

If that doesn't work, try:

```bash
py --version
```

### Check Git

```bash
git --version
```

---

# 🚀 Installation & Setup

## Step 1: Clone the Repository

Open **PowerShell** or **Git Bash** and run:

```bash
git clone https://github.com/tarek-hossain-rifat/ai-lad-project.git
```

Example:

```bash
git clone https://github.com/username/python-project.git
```

Then enter the project folder:

```bash
cd python-project
```

---

## Step 2: Open the Project in VS Code

Run:

```bash
code .
```

If the `code` command does not work, open VS Code manually and select:

**File → Open Folder → Select the project folder**

---

# 🐍 Step 3: Create a Virtual Environment

Creating a virtual environment is recommended so that the project's Python packages do not interfere with other Python projects.

Run:

```bash
python -m venv venv
```

If `python` does not work:

```bash
py -m venv venv
```

This will create a folder named:

```text
venv/
```

---

# ▶️ Step 4: Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt (CMD)

```cmd
venv\Scripts\activate
```

### Git Bash

```bash
source venv/Scripts/activate
```

After activation, you should see something similar to:

```text
(venv) PS C:\project>
```

---

# 📦 Step 5: Install Dependencies

If the project contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

If you want to make sure `pip` is up to date first:

```bash
python -m pip install --upgrade pip
```

Then:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Step 6: Environment Variables

If the project contains a file such as:

```text
.env.example
```

create a copy named:

```text
.env
```

For example:

```text
.env.example
     ↓
.env
```

Then open `.env` and add the required values.

> **Important:** Never upload passwords, API keys, database passwords, or other secrets to GitHub.

---

# ▶️ Step 7: Run the Project

The command depends on the project.

### If the main file is `main.py`

```bash
python main.py
```

### If the project uses `app.py`

```bash
python app.py
```

### If the project uses `run.py`

```bash
python run.py
```

For example:

```bash
python main.py
```

---

# 🖥️ Common Python Project Structures

### Simple Python Project

```text
project/
│
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

Run:

```bash
python main.py
```

---

### Python GUI Project

```text
project/
│
├── main.py
├── gui.py
├── requirements.txt
└── README.md
```

Run:

```bash
python main.py
```

---

### Flask Project

If the project uses Flask, the command may be:

```bash
python app.py
```

or:

```bash
flask run
```

---

### FastAPI Project

If the project uses FastAPI and Uvicorn:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

---

# 🧪 Step 8: Test the Project

After running the project, check whether it works correctly.

For a normal Python application:

```bash
python main.py
```

For a web application, open the URL shown in the terminal.

For example:

```text
http://127.0.0.1:5000
```

or:

```text
http://127.0.0.1:8000
```

---

# 🛑 Step 9: Deactivate Virtual Environment

When you finish working on the project:

```bash
deactivate
```

---

# 🔄 Running the Project Again

The next time you open the project, you do **not** need to create the virtual environment again.

Go to the project directory:

```bash
cd project-folder
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run:

```bash
python main.py
```

---

# ❗ Troubleshooting

## Python is not recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

try:

```bash
py --version
```

If `py` works, use:

```bash
py main.py
```

and:

```bash
py -m venv venv
```

---

## PowerShell Cannot Run Activate.ps1

If you get an execution-policy error, run PowerShell and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## ModuleNotFoundError

Example:

```text
ModuleNotFoundError: No module named 'numpy'
```

First make sure the virtual environment is activated:

```text
(venv)
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, install the missing package manually:

```bash
pip install package-name
```

Example:

```bash
pip install numpy
```

---

## Check Installed Packages

```bash
pip list
```

---

## Create requirements.txt

If the project does not have one:

```bash
pip freeze > requirements.txt
```

---

# 📁 Recommended `.gitignore`

Create a `.gitignore` file:

```gitignore
# Virtual environment
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env

# IDE
.vscode/

# OS
.DS_Store
Thumbs.db
```

---

# 🧹 Clean Installation

If the project is not working correctly, remove the virtual environment and create it again.

### PowerShell

```powershell
Remove-Item -Recurse -Force venv
```

Create it again:

```bash
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

---

# 📌 Quick Start

For most Python projects, the complete setup is:

```bash
git clone https://github.com/tarek-hossain-rifat/ai-lad-project.git
cd YOUR-REPOSITORY
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/tarek-hossain-rifat/`
