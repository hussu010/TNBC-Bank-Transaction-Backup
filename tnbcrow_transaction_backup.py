import requests
import json
from datetime import datetime


now = datetime.now()
date_time = now.strftime('%Y_%m_%d_%H_%M_%S')

f = open(f"tnbcrow_transaction_{date_time}.json", "w")
backup_results = []

next_url = "https://tnbcrow.pythonanywhere.com/recent-trades"

while next_url:
    
    print(next_url)
    
    data = requests.get(f"{next_url}").json()

    results = data["results"]
    
    for result in results:
        backup_results.append(result)
        
    next_url = data["next"]

f.write(json.dumps(backup_results))
f.close()
