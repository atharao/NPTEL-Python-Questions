import os
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Automate staging, committing, and pushing changes")

# Add an argument for the commit message
parser.add_argument("commit_message", help="Commit message for the changes")

# Parse the command-line arguments
args = parser.parse_args()

# Get the list of unstaged files
unstaged_files = os.popen('git status --porcelain').read().splitlines()

# Remove the 'M' or 'A' from the status and get only the file names
unstaged_files = [line[3:] for line in unstaged_files]

# List of files to exclude from staging
exclude_files = ["auto_commit.py"]

# Loop through the unstaged files
for file in unstaged_files:
    if file not in exclude_files:
        os.system(f'git add {file}')
        os.system(f'git commit -m "{args.commit_message}"')
        os.system('git push origin main')

#  python .\auto_commit.py "Fourth Week"
