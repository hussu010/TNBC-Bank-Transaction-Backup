import requests

f = open("bank_backup_01_07_2021.json", "w")

next_url = "http://184.169.226.23/bank_transactions"

while next_url:
    
    print(next_url)
    
    data = requests.get(f"{next_url}").json()

    results = data["results"]
    
    for result in results:
        result = str(result) + ","
        f.write(result)
        
    next_url = data["next"]
    
f.close()
