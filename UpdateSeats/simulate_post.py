import json
import requests 

url 	= 'http://qless.herokuapp.com/update/seat-occupancy/'
# 'http://localhost:8000/update/seat-occupancy/'
r = requests.post(url, json={"sid":[1,2,3,4],"occupancy":[True,False,False,True]})

print(r.status_code)