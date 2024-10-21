# 导包
import re
import os
import requests,  request_type_config
from yunke import global_parame
import unittest
from unittestreport import ddt, json_data, TestRunner

file_path = os.path.dirname((os.path.realpath(__file__)))
# 登录获取token
@ddt
class Test_request_type(unittest.TestCase):
    """
        type1 = 代表把所有请求修改为阻断
        type2 = 代表把所有请求修改为放行
        type3 = 代表把规则修改为关闭状态
        type4 = 代表把规则从关闭状态修改为开启状态
    """
    # @classmethod
    # def setUpClass(cls) -> None:
    #     login_response = requests.post(url=global_parame.login_url, json=global_parame.login_data,
    #                                    headers=global_parame.login_header)
    #     # token设为全局变量
    #     global_parame.token = login_response.json()["data"]["token"]
    #     if login_response.status_code == 200:
    #         print("登录成功。token:", login_response.json()["data"]["token"])
    #         print("-------------------------开始测试---------------------------")
    #         print("\n----------------------------------------------------------------------------------------------\n")
    #     else:
    #         print("登录失败，响应为：", login_response.json())

    # 开启自定义请求方式，阻断所有请求使用放行的方法进行请求
    @json_data(fr"{file_path}\method_block.json")
    def test_method(self, data):
        # 开器自定义请求方式，放行所有请求
        if data["type"] == 1:
            open_rule_response = requests.post(url=request_type_config.request_type_update_url,
                                               json=request_type_config.request_type_update_data_block,
                                               headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            print("响应结果为：", open_rule_response.json())
            print("\n----------------------------------------------------------------------------------------------\n")
            if open_rule_response.json()["message"] == "Success":
                print(f"修改规则成功，响应结果为：{open_rule_response.json()}\n-------开始验证功能生效性--------")
                # 使用不同请求方式验证规则
                method_response = requests.request(data["method"], global_parame.IP)
                print(f"请求方式为：{data['method']}\n触发规则响应码为：{method_response.status_code}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(method_response.text)
                print("re_info", re_info)
                for item in re_info:
                    print(item.groupdict())
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    with open(rf"{file_path}\request_type.txt", 'a+', encoding='utf-8') as f:
                        f.write(
                            f"\n测试用例:\n将所有请求方法设为阻断——{data['title'],}\n日志信息:{dic}\n")
                        print(
                            f"\n测试用例:\n{data['title'],}\n日志信息:{dic}\n")
                self.assertEqual(data["expect"], method_response.status_code)
            else:
                print(f"修改规则失败，响应结果为：{open_rule_response.json()}")

        # 开器自定义请求方式，放行所有请求
        if data["type"] == 2:
            open_rule_response = requests.post(url=request_type_config.request_type_update_url,
                                               json=request_type_config.request_type_update_data_Release,
                                               headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            print("响应结果为：", open_rule_response.json())
            print("\n----------------------------------------------------------------------------------------------\n")
            if open_rule_response.json()["message"] == "Success":
                print(f"修改规则成功，响应结果为：{open_rule_response.json()}\n-------开始验证功能生效性--------")
                # 使用不同请求方式验证规则
                method_response = requests.request(data["method"], global_parame.IP)
                print(f"请求方式为：{data['method']}\n响应码为：{method_response.status_code}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(method_response.text)
                print("re_info", re_info)
                for item in re_info:
                    print(item.groupdict())
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    with open(rf"{file_path}\request_type.txt", 'a+', encoding='utf-8') as f:
                        f.write(
                            f"\n测试用例:\n将所有请求方法设为放行——{data['title'],}\n日志信息:{dic}\n")
                        print(
                            f"\n测试用例:\n{data['title'],}\n日志信息:{dic}\n")
                self.assertEqual(data["expect"], method_response.status_code)
            else:
                print(f"修改规则失败，响应结果为：{open_rule_response.json()}")
        if data["type"] == 3:
            open_rule_response = requests.post(url=request_type_config.request_type_update_url,
                                               json=request_type_config.request_type_update_data_close,
                                               headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            print("响应结果为：", open_rule_response.json())
            print("\n----------------------------------------------------------------------------------------------\n")
            if open_rule_response.json()["message"] == "Success":
                print(f"修改规则成功，响应结果为：{open_rule_response.json()}\n-------开始验证功能生效性--------")
                # 使用不同请求方式验证规则
                method_response = requests.request(data["method"], global_parame.IP)
                print(f"请求方式为：{data['method']}\n响应码为：{method_response.status_code}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(method_response.text)
                print("re_info", re_info)
                for item in re_info:
                    print(item.groupdict())
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    with open(rf"{file_path}\request_type.txt", 'a+', encoding='utf-8') as f:
                        f.write(
                            f"\n测试用例:\n{data['title'],}\n日志信息:{dic}\n")
                        print(
                            f"\n测试用例:\n{data['title'],}\n日志信息:{dic}\n")
                self.assertEqual(data["expect"], method_response.status_code)
            else:
                print(f"修改规则失败，响应结果为：{open_rule_response.json()}")
        if data["type"] == 4:
            open_rule_response = requests.post(url=request_type_config.request_type_update_url,
                                               json=request_type_config.request_type_update_data_open,
                                               headers={"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"})
            print("响应结果为：", open_rule_response.json())
            print("\n----------------------------------------------------------------------------------------------\n")
            if open_rule_response.json()["message"] == "Success":
                print(f"修改规则成功，响应结果为：{open_rule_response.json()}\n-------开始验证功能生效性--------")
                # 使用不同请求方式验证规则
                method_response = requests.request(data["method"], global_parame.IP)
                print(f"请求方式为：{data['method']}\n响应码为：{method_response.status_code}")
                re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                                     r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                                     r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                                     re.S).finditer(method_response.text)
                print("re_info", re_info)
                for item in re_info:
                    print(item.groupdict())
                    dic = item.groupdict()
                    print(f"日志信息为：{dic}")
                    with open(rf"{file_path}\request_type.txt", 'a+', encoding='utf-8') as f:
                        f.write(
                            f"\n测试用例:\n{data['title'],}\n日志信息:{dic}\n")
                        print(
                            f"\n测试用例:\n{data['title'],}\n日志信息:{dic}\n")
                self.assertEqual(data["expect"], method_response.status_code)
            else:
                print(f"修改规则失败，响应结果为：{open_rule_response.json()}")


if __name__ == '__main__':
    # 调试使用
    # unittest.main()
    # 返回当前工作目录
    path = os.path.dirname((os.path.realpath(__file__)))
    # 返回测试用例类的测试结果，加入工作目录路径以及文件名
    suite = unittest.defaultTestLoader.discover(path, pattern="test_request_type.py")
    # TestRunner() 确定测试报告框架，将测试结果嵌套到框架中
    """             
        filename="report.html", 生成测试报告的html文件名称
        report_dir="./reports", 在工作文件的根目录下创建reports目录文件夹存放测试报告文件
        title='测试报告',             
        tester='测试员',             
        desc="XX项目测试生成的报告",             
        templates=1
    """
    runner = TestRunner(suite, title="自定义请求方式测试报告", tester="朱展鹏", desc="云科WAF防火墙", templates=3,
                        report_dir=path)
    # 运行程序，生成报告
    runner.run()

