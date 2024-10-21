"""
 type1 : 新增
 type2 : 修改（触发规则默认为post请求 json格式）
    type2.1：代表修改后使用get请求触发规则
    type2.2：代表修改后使用post from表单格式触发规则
 type3 : 删除
 type4 : 不需要新增、修改、删除、直接触发规则

"""
import datetime
import time
import requests

from yunke import global_parame

# 规则id
id = ""
monitor_id = ""
# 弱口令阻断新增接口
add_rule_url = "/seraph-admin/admin-api/advanced_defense/weak_pwd/add"
# 弱口令监测新增接口
add_weak_monitor = "/seraph-admin/admin-api/weak_pwd/add"
# 弱口令阻断编辑接口
update_rule_url = "/seraph-admin/admin-api/advanced_defense/weak_pwd/update"
# 弱口令监测编辑接口
update_weak_monitor = "/seraph-admin/admin-api/weak_pwd/update"
# 弱口令阻断删除接口
delete_rule_url = "/seraph-admin/admin-api/advanced_defense/weak_pwd/delete"
# 弱口令监测删除接口
delete_weak_monitor = "/seraph-admin/admin-api/weak_pwd/delete"
# 弱口令阻断列表接口
list_rule_url = "/seraph-admin/admin-api/advanced_defense/weak_pwd/list"
# 弱口令监测列表接口
list_weak_monitor = "/seraph-admin/admin-api/weak_pwd/list"
# 弱口令阻断详情接口
get_url = "/seraph-admin/admin-api/advanced_defense/weak_pwd/get"
# 弱口令监测详情接口
get_weak_monitor = "/seraph-admin/admin-api/weak_pwd/get"
# 弱口令日志接口
weak_log = "/seraph-admin/admin-api/log/weak_pwd"
# 正则预加载
info = """<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span 
class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span 
class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span 
class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?"""


def get_weak_pwd_log(app_id, page_num=1, page_size=100, hour=24, action=0):
    if app_id == '':
        raise ValueError("app_id不能为空。")
    else:
        time_info = get_time(hour=hour)
        json_data = {
            "start_time": time_info["front_timestamp"],
            "end_time": time_info["now_timestamp"],
            "action": action,
            "app_id": app_id,
            "page_num": page_num,
            "page_size": page_size,
            "ip": {
                "type": 1,
                "simple_value": "",
                "multi_value": []
            },
            "url": {
                "type": 1,
                "simple_value": "",
                "multi_value": []
            }
        }
        response = requests.post(url=f"http://{global_parame.admin_host}:{global_parame.admin_port}" + weak_log, json=json_data,
                                 headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
        return response.json()


def get_time(hour):
    time_info = {}
    if type(hour) == int:
        # 获取若干小时前的时间戳,默认24小时
        now_time = datetime.datetime.now()
        front_time = now_time - datetime.timedelta(hours=hour)
        front_timestamp = int(front_time.timestamp())
        # 获取当前时间1分钟后的的时间戳
        now_time = datetime.datetime.now()
        last_time = now_time + datetime.timedelta(minutes=1)
        last_timestamp = int(last_time.timestamp())
        time_info["front_timestamp"] = front_timestamp
        time_info["now_timestamp"] = last_timestamp
        return time_info
    else:
        raise TypeError("hour值类型错误。")


def check_log(expect, practical):
    if expect["weak_pwd_url"] == practical["url"] and expect["weak_data"]["password"] == practical["password"]:
        return 405
    else:
        return 200
