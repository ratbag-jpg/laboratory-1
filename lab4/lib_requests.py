import requests
def use_requests():
    res = requests.get("https://httpbin.org/ip")
    print(f"requests: {res.json()}")