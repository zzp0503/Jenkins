import time

import requests

url = "https://ks.ouchn.cn/g/examination/student/stuRegisterExam"

payload = 'stuId=2314001258300&registerType=1&planId=bfe87e0a250f4ab88346b4da11fdbb9d&examPlanCode=202410&stuNo=2314001258300&obeyAllocation=true&registerPlaceBranchId=140&registerPlaceBranchName=%E5%9B%BD%E5%AE%B6%E5%BC%80%E6%94%BE%E5%A4%A7%E5%AD%A6%E5%B1%B1%E8%A5%BF%E5%88%86%E9%83%A8&registerPlaceCollegeId=14000&registerPlaceCollegeName=%E7%9C%81%E6%A0%A1%E7%9B%B4%E5%B1%9E%E9%83%A8&registerPlaceCenterId=1400000&registerPlaceCenterName=%E7%9C%81%E6%A0%A1%E7%9B%B4%E5%B1%9E%20%E5%AD%A6%E4%B9%A0%E4%B8%AD%E5%BF%83&registerPlaceId=1400001&registerPlaceName=%E5%B1%B1%E8%A5%BF%E5%BC%80%E5%A4%A7%E7%9B%B4%E5%B1%9E%E5%AD%A6%E4%B9%A0%E4%B8%AD%E5%BF%83'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': 'student_pcNbWcFnz6mHM7iidr43REbdDUurwzW21qr7begTi0i8k=',
    'Cookie': 'HWWAFSESID=beb7f7f92ca5fd5ce2; HWWAFSESTIME=1712884920088'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.json())

while True:
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.json())
    if response.json()["code"] != 2:
        break
    else:
        time.sleep(2)
