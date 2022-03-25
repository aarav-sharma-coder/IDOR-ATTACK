import requests

for i in range(1,5000):

    URL = f"http://ec2-3-111-8-121.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"

    request = requests.get(url = URL) 
    
    if request.status_code == 200:
        print(URL)