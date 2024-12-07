import requests
import json
import os

API_KEY = "******"
ID_CHANNEL = "******"

url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={ID_CHANNEL}&key={API_KEY}"

response = requests.request("GET", url)
print(json.dumps(response.json(), indent=4, sort_keys=True))

output_dir = "/******/youtube_airflow/datalake/bronze"
output_file = os.path.join(output_dir, "channels.json")

os.makedirs(output_dir, exist_ok=True)

with open(output_file, "w") as outfile:
    json.dump(response.json(), outfile)