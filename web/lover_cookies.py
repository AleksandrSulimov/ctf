# CodeBy Любитель печений
import requests
url = "http://62.173.140.174:16047/"
session = requests.Session()
cookies_data = {
        "cookies": "[Sugar cookies, Oatmeal cookies, Crackers cookies]",
        "amount": '[1, 5, 2]'
    }
response = session.get(url, cookies=cookies_data)
print(response.text)
session.close()
