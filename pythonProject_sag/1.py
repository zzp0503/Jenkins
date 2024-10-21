import time

import requests
import datetime

header = {
    "User-Agent": "Ask Jeeves"
}

# print(response.text)

for i in range(1):
    for ii in range(5):
        response = requests.get(url="http://sag.seraph.ac.cn:8022/shtml/99/zh/index.html")
        print(f"{ii+1}:{response.status_code}——————{datetime.datetime.now()}")
    for ii in range(6):
        response = requests.get(url="http://sag.seraph.ac.cn:8022/shtml/99/zh/index.html")
        print(f"{ii+1}:{response.status_code}——————{datetime.datetime.now()}")

    # while True:
    #     response = requests.get(url="http://sag.seraph.ac.cn:8022/shtml/99/zh/index.html")
    #     print(f"{response.status_code}————{datetime.datetime.now()}")
    #     if response.status_code == 200:
    #         break
    #     else:
    #         time.sleep(1)


