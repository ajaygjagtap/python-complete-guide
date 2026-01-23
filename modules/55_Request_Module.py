''' 
It is library for HTTP requests.
Used to communicate with APIs / web servers.


Common HTTP Methods :                     API Status Codes (Most Imp.) :
GET    -----> Fetch data                  200 -------> Ok (Success)
POST   -----> Insert data                 201 -------> Created (New resource)
PUT    -----> Update full data            400 -------> Bad Request
PATCH  -----> Update partial data         401 -------> Unauthorized
DELETE -----> Remove data                 404 -------> Not Found
                                          500 -------> Server Error
'''


import requests

response = requests.get("https://www.google.com")
print(response.text)

print("-----------------------------------------------------------------------------")

# Simple GET request example
url_1 = "https://api.github.com"
response_1 = requests.get(url)

print(response_1.status_code)
print(response_1.text)

print("-----------------------------------------------------------------------------")

# Simple POST request example
url_2 = "https://httpbin.org?post"
data = {"name" : "Alice", "Age" : 22}

response_2 = requests.post(url_1, data = data)

print(response_2.status_code)
print(response_2.json())

print("-----------------------------------------------------------------------------")

# Download img file example
url_3 = "https://httpbin.org/image/png"

response_3 = requests.get(url_3)

open(f"img_file/file.png", "wb").write(response_3.content)
