import json
import requests 

r = requests.post('http://localhost:8000/update/seat-occupancy/', json={"sid":[1,2,3,4],"occupancy":[False,False,False,False]})

print(r.status_code)