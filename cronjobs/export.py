import requests
import logging
from datetime import datetime

# Set up logging
log_file = '/Users/abbal/abbaldhakal/cronjobs/export.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(level, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_func = getattr(logging, level)
    log_func(f"{timestamp} - {message}")

# Replace with your file ID and API key
file_id = '18z44pt-Oorirwj0TynrswHEEoZfF7b2B'
api_key = 'AIzaSyAuuUS75DPQDGXrVZrXtsuZMzQy2Nj1o2Q'

url = f'https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={api_key}'
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    with open('/Users/abbal/abbaldhakal/data/scholarships.json', 'w') as f:
        f.write(response.text)
    log_message('info', 'File downloaded successfully.')
except requests.ConnectionError:
    log_message('error', 'Failed to download file: No internet connection.')
except requests.Timeout:
    log_message('error', 'Failed to download file: Request timed out.')
except requests.RequestException as e:
    log_message('error', f'Failed to download file: {e}')
except Exception as e:
    log_message('error', f'An unexpected error occurred: {e}')