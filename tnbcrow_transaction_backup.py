import requests
import json
from datetime import datetime


now = datetime.now()
date_time = now.strftime('%Y_%m_%d_%H_%M_%S')

f = open(f"tnbcrow_transaction_{date_time}.json", "w")

next_url = "https://tnbcrow.pythonanywhere.com/recent-trades"

while next_url:
    
    print(next_url)
    
    data = requests.get(f"{next_url}").json()

    results = data["results"]
    
    for result in results:
        result = str(result) + ","
        f.write(result)
        
    next_url = data["next"]

f.close()
