import requests

#response = requests.get("https://httpbin.org/get?name=Mike&age=25")

#print(response.status_code)

#res_json = response.json()
#print(res_json)

### send the request with params

payload = {
    "name": "Mike",
    "age" : 25
}
response = requests.get("https://httpbin.org/status/500")

if response.status_code == requests.codes.not_found:
    print("Not Found")
else:
    print(response.status_code)





#res_json = response.json()
#print(res_json)


