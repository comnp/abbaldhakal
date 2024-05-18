import subprocess
import os
import logging
from datetime import datetime

# Set up logging
log_file = '/Users/abbal/abbaldhakal/cronjobs/git.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(level, message):
    log_func = getattr(logging, level)
    log_func(message)

# Define the path to your repository and the specific file
repo_path = '/Users/abbal/abbaldhakal/'
file_to_commit = 'data/scholarships.json'
ssh_key_path = '/Users/abbal/gitkey'  # Path to your custom SSH key

try:
    # Change to the repository directory
    os.chdir(repo_path)
    log_message('info', f'Changed directory to {repo_path}')

    # Ensure only the specific file is staged
    result = subprocess.run(['git', 'add', file_to_commit], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    log_message('info', f'File {file_to_commit} added to git staging area. Output: {result.stdout}, Error: {result.stderr}')

    # Commit the changes if there are any
    commit_message = 'Automated commit and push for scholarships.json'
    result = subprocess.run(['git', 'commit', '-m', commit_message], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        log_message('info', f'Committed changes with message: {commit_message}. Output: {result.stdout}, Error: {result.stderr}')
        
        # Push the changes using the custom SSH key
        result = subprocess.run(['git', 'push', 'origin', 'main'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env={'GIT_SSH_COMMAND': f'ssh -i {ssh_key_path}'})
        log_message('info', 'File committed and pushed successfully.')
        log_message('info', f'git push output: {result.stdout}')
    else:
        log_message('info', 'No changes to commit.')
except subprocess.CalledProcessError as e:
    log_message('error', f'Command "{e.cmd}" failed with return code {e.returncode}. Output: {e.output}, Error: {e.stderr}')
except Exception as e:
    log_message('error', f'An unexpected error occurred: {e}')