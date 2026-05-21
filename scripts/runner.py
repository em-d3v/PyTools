"""
File: runner.py
Date: 05/13/2026
Author: Elena Miller
this script runs the main application
"""


from datetime import datetime
import subprocess
import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))
from config import settings as s


project_dir = Path(__file__).parent.parent  # Get the directory of the current script
# log_file = # Define the log file path

#paths to files
paths = {
    "main": s.MAIN_FILE,
    "log":  os.path.join(s.DIRS["log"], "runner.log") 
}


# make log directory if it doesn't exist
os.makedirs(s.DIRS["log"], exist_ok=True)
#capture output
result = subprocess.run(
[sys.executable, paths["main"]],
capture_output=True,
text=True
)
#log entry
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

