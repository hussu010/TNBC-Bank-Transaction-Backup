import requests
from datetime import date

filename = f"bank_backup_{date.today()}"
BANK_IP = '13.233.77.254'

f = open(f"{filename}.json", "w")

next_url = f"http://{BANK_IP}/bank_transactions"

while next_url:
    
    print(next_url)
    
    data = requests.get(f"{next_url}").json()

    results = data["results"]
    
    for result in results:
        result = str(result) + ","
        f.write(result)
        
    next_url = data["next"]
    
f.close()
