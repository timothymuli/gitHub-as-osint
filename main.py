import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL of the target you are investigating
TARGET_URL = "https://example.com" 

def run_osint_check():
    try:
        # 1. Fetch the website data
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        
        # 2. Parse the HTML to find the Title
        soup = BeautifulSoup(response.text, 'html.parser')
        page_title = soup.title.string if soup.title else "No Title Found"
        
        # 3. Get server info (reveals tech stack like Nginx or Cloudflare)
        server = response.headers.get('Server', 'Unknown Server')

        # 4. Prepare the log entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Title: {page_title} | Server: {server}\n"

        # 5. Append to your log file
        with open("data_log.txt", "a") as f:
            f.write(log_entry)
            
        print(f"Successfully logged data for {TARGET_URL}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_osint_check()
