import requests

# Example: Pulling target metadata from a public API
response = requests.get("https://example.com")
with open("data_log.txt", "a") as f:
    f.write(response.text + "\n")
