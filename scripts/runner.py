"""
File: runner.py
Date: 05/13/2026
Author: Elena Miller
this script runs the main application
"""


import subprocess
import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))
from config import settings as s
project_dir = Path(__file__).parent.parent  # Get the directory of the current script


#paths to files
paths = {
    "main": s.MAIN_FILE,
    
}

# make log directory if it doesn't exist
os.makedirs(s.LOG_DIR, exist_ok=True)
os.makedirs(s.BIN_DIR, exist_ok=True)
#capture output
result = subprocess.run(
[sys.executable, paths["main"]],
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
text=True
)
print("Output:", result.stdout)
print("Errors:", result.stderr)

