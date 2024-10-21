import os
import re
import time
import unittest

import requests
from unittestreport import ddt, json_data, TestRunner

file_path = os.path.dirname((os.path.realpath(__file__)))
from yunke import global_parame
import weak_password_config

admin_ip = global_parame.admin_ip
proxy_ip = global_parame.proxy_ip


@ddt
class Test_weak_password(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     login_response = requests.post(url=global_parame.login_url, json=global_parame.login_data,
    #                                    headers=global_parame.login_header)
    #     # token设为全局变量
    #     global_parame.token = login_response.json()["data"]["token"]
    #     if login_response.json()["code"] == 200:
    #         print("登录成功。token:", login_response.json()["data"]["token"])
    #         print("-------------------------开始测试---------------------------")
    #         print("\n----------------------------------------------------------------------------------------------\n")
    #     else:
    #         print("登录失败，响应为：", login_response.json())

    @json_data(f"{file_path}\weak_password.json")
    def test_weak(self, data):
        if data["type"] == 1:
            # 新增规则
            add_rule_data = {
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            add_response = requests.post(url=admin_ip + weak_password_config.add_rule_url, json=add_rule_data,
                                         headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if add_response.json()["code"] == 200:
                print("新增规则成功，响应结果为：", add_response.json())
                # 调用列表接口获取规则id
                list_data = {
                    "page_num": 1,
                    "page_size": 20,
                    "app_id": global_parame.app_id
                }
                list_response = requests.post(url=admin_ip + weak_password_config.list_rule_url,
                                              headers={"open_api_token": global_parame.open_api_token,
                                                       "Content-Type": "application/json"},
                                              json=list_data)
                print("\n------------------------------------------------------------------------------\n")
                print("创建的规则id为：", list_response.json()["data"]["list"][0]["id"])
                weak_password_config.id = list_response.json()["data"]["list"][0]["id"]
                time.sleep(2)
                # 调用代理IP，触发规则
                test_response = requests.post(url=proxy_ip + data["weak_pwd_url"],
                                              headers={"Content-Type": "application/json"},
                                              json=data["weak_data"])
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                print(f"触发规则响应码为：{test_response.status_code}，预期结果响应码为：{data['expect']}")
                print(weak_password_config.info)
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(test_response.text)
                for item in re_info:
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], test_response.status_code)
            else:
                print("新增规则失败，响应结果为：", add_response.json())

        elif data["type"] == 2:
            # 编辑规则
            update_rule_data = {
                "id": weak_password_config.id,
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            update_response = requests.post(url=admin_ip + weak_password_config.update_rule_url, json=update_rule_data,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if update_response.json()["code"] == 200:
                print("\n------------------------------------------------------------------------------\n")
                print("编辑规则成功，响应结果为：", update_response.json())
                time.sleep(2)
                # 调用代理IP，触发规则
                test_response = requests.post(url=proxy_ip + data["weak_pwd_url"],
                                              headers={"Content-Type": "application/json"},
                                              json=data["weak_data"])
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                print(f"触发规则响应码为：{test_response.status_code}，预期结果响应码为：{data['expect']}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(test_response.text)
                for item in re_info:
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], test_response.status_code)
            else:
                print("编辑规则失败，响应结果为：", update_response.json())
        elif data["type"] == 2.1:
            # 编辑规则
            update_rule_data = {
                "id": weak_password_config.id,
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            update_response = requests.post(url=admin_ip + weak_password_config.update_rule_url, json=update_rule_data,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if update_response.json()["code"] == 200:
                print("\n------------------------------------------------------------------------------\n")
                print("编辑规则成功，响应结果为：", update_response.json())
                time.sleep(2)
                # 调用代理IP，触发规则
                test_response = requests.get(url=proxy_ip + data["weak_pwd_url"],
                                             )
                print(data["title"])
                print(f"触发规则响应码为：{test_response.status_code}，预期结果响应码为：{data['expect']}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(test_response.text)
                for item in re_info:
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], test_response.status_code)
            else:
                print("编辑规则失败，响应结果为：", update_response.json())
        elif data["type"] == 2.2:
            # 编辑规则
            update_rule_data = {
                "id": weak_password_config.id,
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            update_response = requests.post(url=admin_ip + weak_password_config.update_rule_url, json=update_rule_data,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if update_response.json()["code"] == 200:
                print("\n------------------------------------------------------------------------------\n")
                print("编辑规则成功，响应结果为：", update_response.json())
                time.sleep(2)
                # 调用代理IP，触发规则
                weak_data = data["weak_data"]
                test_response = requests.post(url=proxy_ip + data["weak_pwd_url"], data=weak_data,
                                              headers={"Content-Type": "application/x-www-form-urlencoded"}
                                              )
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                print(f"触发规则响应码为：{test_response.status_code}，预期结果响应码为：{data['expect']}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(test_response.text)
                for item in re_info:
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], test_response.status_code)
            else:
                print("编辑规则失败，响应结果为：", update_response.json())


        elif data["type"] == 3:
            # 调用删除接口
            delete_data = {
                "id": weak_password_config.id
            }
            delete_response = requests.post(url=admin_ip + weak_password_config.delete_rule_url,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"},
                                            json=delete_data)
            print(f"响应数据为：{delete_response.json()}")
            get_response = requests.post(url=admin_ip + weak_password_config.get_url,
                                         headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"},
                                         json=delete_data)
            # 通过调用查询接口查看是否删除成功
            if get_response.json()["message"] == "数据不存在":
                print("\n------------------------------------------------------------------------------\n")
                print(f"删除规则成功，查询接口调用响应结果为：{get_response.json()['message']}")
                time.sleep(2)
                # 调用代理IP
                weak_data = data["weak_data"]
                test_response = requests.post(url=proxy_ip + data["weak_pwd_url"], data=weak_data,
                                              headers={"Content-Type": "application/x-www-form-urlencoded"}
                                              )
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                print(f"触发规则响应码为：{test_response.status_code}，预期结果响应码为：{data['expect']}")
                print(test_response.text)
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(test_response.text)
                for item in re_info:
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    print("\n------------------------------------------------------------------------------\n")
            else:
                print("\n------------------------------------------------------------------------------\n")
                print("删除数据失败，响应为：", get_response.json())
                print("\n------------------------------------------------------------------------------\n")
        elif data["type"] == 4:
            time.sleep(2)
            test_response = requests.post(url=proxy_ip + data["weak_pwd_url"],
                                          headers={"Content-Type": "application/json"},
                                          json=data["weak_data"])
            print("\n------------------------------------------------------------------------------\n")
            print("请求参数为：", data["weak_data"])
            print(data["title"])
            print(f"触发规则响应码为：{test_response.status_code}，预期结果响应码为：{data['expect']}")
            re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                 r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                 r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                 r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                 re.S).finditer(test_response.text)
            for item in re_info:
                dic = item.groupdict()
                print(f"日志信息为：{dic}")
                print("\n------------------------------------------------------------------------------\n")
            self.assertEqual(data["expect"], test_response.status_code)

    @json_data(f"{file_path}\monitor_weak_pwd.json")
    def test_weak_monitor(self, data):
        if data["type"] == 1:
            # 新增规则
            add_rule_data = {
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            add_response = requests.post(url=admin_ip + weak_password_config.add_weak_monitor, json=add_rule_data,
                                         headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if add_response.json()["code"] == 200:
                print("新增规则成功，响应结果为：", add_response.json())
                # 调用列表接口获取规则id
                list_data = {
                    "page_num": 1,
                    "page_size": 20,
                    "app_id": global_parame.app_id
                }
                list_response = requests.post(url=admin_ip + weak_password_config.list_weak_monitor,
                                              headers={"open_api_token": global_parame.open_api_token,
                                                       "Content-Type": "application/json"},
                                              json=list_data)
                print("\n------------------------------------------------------------------------------\n")
                print("创建的规则id为：", list_response.json()["data"]["list"][0]["id"])
                weak_password_config.monitor_id = list_response.json()["data"]["list"][0]["id"]
                time.sleep(2)
                # 调用代理IP，触发规则
                requests.post(url=proxy_ip + data["weak_pwd_url"],
                              headers={"Content-Type": "application/json"},
                              json=data["weak_data"])
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                time.sleep(60)
                weak_log = weak_password_config.get_weak_pwd_log(app_id=global_parame.app_id, action=200)
                print(weak_log["data"]["list"][0])
                practical = weak_password_config.check_log(expect=data, practical=weak_log["data"]["list"][0])
                self.assertEqual(data["expect"], practical)
            else:
                print("新增规则失败，响应结果为：", add_response.json())

        elif data["type"] == 2:
            # 编辑规则
            update_rule_data = {
                "id": weak_password_config.monitor_id,
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            update_response = requests.post(url=admin_ip + weak_password_config.update_weak_monitor,
                                            json=update_rule_data,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if update_response.json()["code"] == 200:
                print("\n------------------------------------------------------------------------------\n")
                print("编辑规则成功，响应结果为：", update_response.json())
                time.sleep(2)
                # 调用代理IP，触发规则
                requests.post(url=proxy_ip + data["weak_pwd_url"],
                              headers={"Content-Type": "application/json"},
                              json=data["weak_data"])
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                time.sleep(60)
                weak_log = weak_password_config.get_weak_pwd_log(app_id=global_parame.app_id, action=200)
                print(weak_log["data"]["list"][0])
                practical = weak_password_config.check_log(expect=data, practical=weak_log["data"]["list"][0])
                print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], practical)
            else:
                print("编辑规则失败，响应结果为：", update_response.json())
        elif data["type"] == 2.1:
            # 编辑规则
            update_rule_data = {
                "id": weak_password_config.monitor_id,
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            update_response = requests.post(url=admin_ip + weak_password_config.update_weak_monitor,
                                            json=update_rule_data,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if update_response.json()["code"] == 200:
                print("\n------------------------------------------------------------------------------\n")
                print("编辑规则成功，响应结果为：", update_response.json())
                time.sleep(2)
                # 调用代理IP，触发规则
                requests.get(url=proxy_ip + data["weak_pwd_url"], params=data["weak_data"])
                print(data["title"])
                time.sleep(50)
                weak_log = weak_password_config.get_weak_pwd_log(app_id=global_parame.app_id, action=200)
                print(weak_log["data"]["list"][0])
                practical = weak_password_config.check_log(expect=data, practical=weak_log["data"]["list"][0])
                print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], practical)
            else:
                print("编辑规则失败，响应结果为：", update_response.json())
        elif data["type"] == 2.2:
            # 编辑规则
            update_rule_data = {
                "id": weak_password_config.monitor_id,
                "account_field": data["rule_data"]["account_field"],
                "password_field": data["rule_data"]["password_field"],
                "encrypt_type": data["rule_data"]["encrypt_type"],
                "match": {
                    "len": data["rule_data"]["match"]["len"],
                    "num": data["rule_data"]["match"]["num"],
                    "upper": data["rule_data"]["match"]["upper"],
                    "lower": data["rule_data"]["match"]["lower"],
                    "letter": data["rule_data"]["match"]["letter"],
                    "punctuation": data["rule_data"]["match"]["punctuation"],
                    "name_pwd_equal": data["rule_data"]["match"]["name_pwd_equal"],
                    "continuous_char": data["rule_data"]["match"]["continuous_char"]
                },
                "identify_code": data["rule_data"]["identify_code"],
                "identify_key_word": data["rule_data"]["identify_key_word"],
                "url": data["rule_data"]["url"],
                "status": data["rule_data"]["status"],
                "action": data["rule_data"]["action"],
                "description": data["rule_data"]["description"],
                "app_id": global_parame.app_id
            }
            update_response = requests.post(url=admin_ip + weak_password_config.update_weak_monitor,
                                            json=update_rule_data,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            if update_response.json()["code"] == 200:
                print("\n------------------------------------------------------------------------------\n")
                print("编辑规则成功，响应结果为：", update_response.json())
                time.sleep(2)
                # 调用代理IP，触发规则
                weak_data = data["weak_data"]
                requests.post(url=proxy_ip + data["weak_pwd_url"], data=weak_data,
                              headers={"Content-Type": "application/x-www-form-urlencoded"}
                              )
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                time.sleep(50)
                weak_log = weak_password_config.get_weak_pwd_log(app_id=global_parame.app_id, action=200)
                print(weak_log["data"]["list"][0])
                practical = weak_password_config.check_log(expect=data, practical=weak_log["data"]["list"][0])
                print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], practical)
            else:
                print("编辑规则失败，响应结果为：", update_response.json())


        elif data["type"] == 3:
            # 调用删除接口
            delete_data = {
                "id": weak_password_config.monitor_id
            }
            delete_response = requests.post(url=admin_ip + weak_password_config.delete_weak_monitor,
                                            headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"},
                                            json=delete_data)
            print(f"响应数据为：{delete_response.json()}")
            get_response = requests.post(url=admin_ip + weak_password_config.get_weak_monitor,
                                         headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"},
                                         json=delete_data)
            # 通过调用查询接口查看是否删除成功
            if get_response.json()["message"] == "数据不存在":
                print("\n------------------------------------------------------------------------------\n")
                print(f"删除规则成功，查询接口调用响应结果为：{get_response.json()['message']}")
                time.sleep(2)
                # 调用代理IP
                weak_data = data["weak_data"]
                requests.post(url=proxy_ip + data["weak_pwd_url"], data=weak_data,
                              headers={"Content-Type": "application/x-www-form-urlencoded"}
                              )
                print(data["title"])
                print("请求参数为：", data["weak_data"])
                time.sleep(60)
                weak_log = weak_password_config.get_weak_pwd_log(app_id=global_parame.app_id, action=200)
                print(weak_log["data"]["list"][0])
                practical = weak_password_config.check_log(expect=data, practical=weak_log["data"]["list"][0])
                print("\n------------------------------------------------------------------------------\n")
                self.assertEqual(data["expect"], practical)
            else:
                print("\n------------------------------------------------------------------------------\n")
                print("删除数据失败，响应为：", get_response.json())
                print("\n------------------------------------------------------------------------------\n")
        elif data["type"] == 4:
            time.sleep(2)
            requests.post(url=proxy_ip + data["weak_pwd_url"],
                          headers={"Content-Type": "application/json"},
                          json=data["weak_data"])
            print("\n------------------------------------------------------------------------------\n")
            print(data["title"])
            print("请求参数为：", data["weak_data"])
            time.sleep(60)
            weak_log = weak_password_config.get_weak_pwd_log(app_id=global_parame.app_id, action=200)
            print(weak_log["data"]["list"][0])
            practical = weak_password_config.check_log(expect=data, practical=weak_log["data"]["list"][0])
            print("\n------------------------------------------------------------------------------\n")
            self.assertEqual(data["expect"], practical)


if __name__ == '__main__':
    # 调试使用
    # unittest.main()
    # 返回当前工作目录
    path = os.path.dirname(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))
    # 返回测试用例类的测试结果，加入工作目录路径以及文件名
    suite = unittest.defaultTestLoader.discover(path, pattern="test_weak_password.py")
    # TestRunner() 确定测试报告框架，将测试结果嵌套到框架中
    """
        filename="report.html", 生成测试报告的html文件名称
        report_dir="./reports", 在工作文件的根目录下创建reports目录文件夹存放测试报告文件
        title='测试报告',
        tester='测试员',
        desc="XX项目测试生成的报告",
        templates=1
    """
    runner = TestRunner(suite, title="弱口令防御测试报告", tester="朱展鹏", desc="云科WAF防火墙", templates=3,
                        report_dir=path)
    # 运行程序，生成报告
    runner.run()
