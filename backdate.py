import os
import random
from datetime import datetime, timedelta
from git import Repo

# Configuration
REPO_PATH = os.getcwd()  # Automatically sets the current directory
COMMITS_PER_DAY = 2  # Number of commits per day
START_DATE = datetime(2023, 5, 1)  # Start date (January 1st, 2024)
END_DATE = datetime(2024, 7, 15)  # End date (July 15th, 2024)

# Initialize the repo
repo = Repo(REPO_PATH)

# Calculate total days in the range
total_days = (END_DATE - START_DATE).days + 1

for day in range(total_days):
    commit_date = START_DATE + timedelta(days=day)
    for _ in range(COMMITS_PER_DAY):
        # Randomize time within the day
        commit_time = commit_date + timedelta(seconds=random.randint(0, 86400))
        formatted_time = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

        # Create a dummy file
        file_name = f"dummy_file_{day}_{_}.txt"
        file_path = os.path.join(REPO_PATH, file_name)
        with open(file_path, "w") as f:
            f.write(f"Commit made on {formatted_time}")

        # Add the file to the repo
        repo.git.add(file_path)

        # Set environment variables for commit dates
        os.environ["GIT_AUTHOR_DATE"] = formatted_time
        os.environ["GIT_COMMITTER_DATE"] = formatted_time

        # Make the commit
        repo.index.commit(f"Backdated commit on {formatted_time}")

print("Backdated commits complete!")
