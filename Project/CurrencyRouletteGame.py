import requests
def call_exchangerates():

 url = "https://anyapi.io/api/v1/exchange/convert?base=USD&to=ILS&amount=1&apiKey=kmgperaohggrli9rpdpi0gdsjpobu5angf7r7b5rabb4o19god6ul8"

 payload = {}
 headers = {}

 response = requests.request("GET", url, headers=headers, data=payload)
 json_response = response.json()
 print(json_response["converted"])
 return json_response["converted"]



