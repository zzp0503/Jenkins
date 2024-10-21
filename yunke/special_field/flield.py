import datetime
import re
import requests


def req():
    """
    "HOST": "www.baidu.com"
    "Content-Type":"application/json"
    "Origin":"https://ntp.msn.cn"
    "User-Agent": "Chrome/118.0.0.0 Safari"
    "Cookie": "SPHPSESSIDS=9o47u8p03k0o47tepgum5e16n6;ASSA=55"
    "Referer": "https://www.baidu.com/test01"
    "Content-Type": "text/html;charset=utf-8"
    "Content-Length": "3911"
    "X-Direct-IP": "192.168.3.141"  //用户IP
    "X-Forwarded-For": "192.168.3.11"
    "Origin": "http://192.168.3.15"
    "Accept-Language": "zh-CN,zh;q=0.9"
    "Authorization": "bc410942430054OTShiBsWUik44wRPNeGvVCs4lWNyTnOK"
    """
    req_url = "http://106.15.37.76/vul/xss/xss_reflected_get.php?name=22"
    req_head = {"X-REAL-IP": "192.168.3.11","Cookie": "SPHPSESSIDS=9o47u8p03k0o47tepgum5e16n6"}
    req_data = {"name.txt": "admidn"}
    res = requests.request('POST', req_url, headers=req_head,json=req_data)
    if res.status_code == 405:
        print(f"请求被拦截：响应码为：{res.status_code}")
        print(f"请求时间为：{datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}")
        print(f"请求hearer为：{req_head}")
        print(f"请求数据为：{req_data}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(res.text)

        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
    else:
        print(f"请求成功，未被拦截：响应码为：{res.status_code}")
        print(f"请求时间为：{datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}")
        print(f"请求hearer为：{req_head}")
        print(f"请求数据为：{req_data}")


if __name__ == '__main__':
    req()
