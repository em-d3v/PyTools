"""
File: builder.py
Date: 05/17/2026   
Author: Elena Miller
This script compiles the source code into a single executable file using PyInstaller.
"""
from datetime import datetime
import subprocess
import sys
import os
from pathlib import Path
# import constants as const
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))
from config import settings as s


project_dir = Path(__file__).parent.parent  # Get the directory of the current script
# log_file = # Define the log file path

#paths to files
paths = {
    "main": s.SOURCE_FILE,
    "log":  os.path.join(s.DIRECTORY["project"], s.DIRECTORY["log"], "builder.log"),
    "output": os.path.join(s.DIRECTORY["project"], s.DIRECTORY["build"])
}

command = ["pyinstaller",
            "--onefile",    paths["main"], 
            "-n",           s.TARGET["name"],
            "--distpath",   s.TARGET["dir"],
            "--specpath",   s.TARGET["build"],
            "--clean",
        ]
# make log directory if it doesn't exist
os.makedirs(s.DIRECTORY["log"], exist_ok=True)
#capture output
print("Building Executable...")
result = subprocess.run(command, capture_output=True)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = (
    f"\n--- Run at {timestamp} ---\n"
    f"STDOUT:\n{result.stdout}\n"
    f"STDERR:\n{result.stderr}\n"
)
with open(paths["log"], "w") as f:
        f.write(log_entry)
print("Output:", result.stdout)
print("Errors:", result.stderr)

