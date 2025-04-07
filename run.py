import os
import sys
import subprocess
import venv

VENV_DIR = ".venv"

def create_venv():
    if not os.path.isdir(VENV_DIR):
        print("Creating virtual environment...")
        venv.create(VENV_DIR, with_pip=True)
        pip_exe = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "pip")
        subprocess.check_call([pip_exe, "install", "-r", "requirements.txt"])

def run_main():
    python_exe = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin", "python")
    subprocess.check_call([python_exe, "main.py"])

if __name__ == "__main__":
    create_venv()
    run_main()
