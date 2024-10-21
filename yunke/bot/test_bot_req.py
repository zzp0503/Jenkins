import requests
import data_config
from unittestreport import ddt, json_data, TestRunner
import unittest, os,re
from typing import Union
import time,datetime
from yunke import global_parame


@ddt
class Test_bot(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     response = requests.post(url=global_parame.login_url, json=global_parame.login_data, headers=global_parame.login_header)
    #     global_parame.token = response.json()["data"]["token"]
    #     if response.json()["code"] == 200:
    #         print("登录成功。token:", response.json()["data"]["token"])
    #         print("-------------------------开始测试---------------------------")
    #         print("\n----------------------------------------------------------------------------------------------\n")
    #     else:
    #         print("登录失败", response.json())


    @json_data(r"D:\data\python_data\pythonProject\yunke\bot\Trusted_Bot.json")
    def test_Trusted_Bot(self, data):
        print(f"----------测试受信任机器人(精准匹配),签名为:{data['title']}----------")
        trusted_bot_url = data_config.Trusted_Bot_url
        trusted_bot_head = {"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"}
        trusted_response = requests.post(url=trusted_bot_url, headers=trusted_bot_head,
                                         json=data_config.Trusted_Bot_data)
        if trusted_response.json()["code"] == 200:
            print("修改成功，响应码为:", trusted_response.status_code)
        else:
            print("修改失败,响应为:", trusted_response.json())
        response = requests.post(url=data_config.test_url, headers=data["header"])
        time.sleep(1)
        print(f"触发签名的值为：header={data['header']},触发规则返回的响应码：{response.status_code}\n时间:{datetime.datetime.now()}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(response.text)
        print("re_info", re_info)
        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
            print(f"日志信息为：{dic}")
            with open(r"bot_logs", 'a+', encoding='utf-8') as f:
                f.write(
                    f"\n测试用例:测试受信任机器人(精准匹配),签名为:{data['title']}\n接口传参为:{data_config.Trusted_Bot_data}\n请求URL:{data_config.test_url}\n请求头：{data['header']}\n日志信息:{dic}\n")
        print("\n----------------------------------------------------------------------------------------------\n")
        self.assertEqual(405, response.status_code)

    @json_data(r"D:\data\python_data\pythonProject\yunke\bot\Untrusted_Bot.json")
    def test_Untrusted_Bot(self, data):
        print(f"----------测试不受信任机器人(精准匹配),签名为:{data['title']}----------")
        untrusted_bot_url = data_config.Untrusted_url
        untrusted_bot_head = {"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"}
        untrusted_response = requests.post(url=untrusted_bot_url, headers=untrusted_bot_head,
                                           json=data_config.Untrusted_data)
        if untrusted_response.json()["code"] == 200:
            print("修改成功，响应码为:", untrusted_response.status_code)
        else:
            print("修改失败,响应为:", untrusted_response.json())
        response = requests.get(url=data_config.test_url, headers=data["header"], data=data["data"])
        print(f"触发签名的值为：header={data['header']},data={data['data']},触发规则返回的响应码：{response.status_code}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(response.text)
        print("re_info", re_info)
        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
            print(f"日志信息为：{dic}")
            with open(r"bot_logs", 'a+', encoding='utf-8') as f:
                f.write(
                    f"\n测试用例:测试不受信任机器人(精准匹配),签名为:{data['title']}\n接口传参为:{data_config.Untrusted_data}\n请求URL:{data_config.test_url}\n请求头：{data['header']}\n请求参数:{data['data']}\n日志信息:{dic}\n")
        print("\n----------------------------------------------------------------------------------------------\n")
        self.assertEqual(405, response.status_code)

    @json_data(r"D:\data\python_data\pythonProject\yunke\bot\Malicious_Bot.json")
    def test_Malicious_Bot(self, data: Union[None, dict]):
        print(f"----------测试恶意任机器人(精准匹配),签名为:{data['title']}----------")
        malicious_bot_url = data_config.Malicious_Bot_url
        malicious_bot_head = {"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"}
        malicious_response = requests.post(url=malicious_bot_url, headers=malicious_bot_head,
                                           json=data_config.Malicious_Bot_data)
        if malicious_response.json()["code"] == 200:
            print("修改成功，响应码为:", malicious_response.status_code)
        else:
            print("修改失败,响应为:", malicious_response.json())
        response = requests.post(url=data_config.test_url, headers=data["header"], data=data["data"])
        print(f"触发签名的值为：header={data['header']},data={data['data']},触发规则返回的响应码：{response.status_code}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(response.text)
        print("re_info", re_info)
        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
            print(f"日志信息为：{dic}")
            with open(r"bot_logs", 'a+', encoding='utf-8') as f:
                f.write(
                    f"\n测试用例:测试恶意的机器人(精准匹配),签名为:{data['title']}\n接口传参为:{data_config.Malicious_Bot_data}\n请求URL:{data_config.test_url}\n请求头：{data['header']}\n请求参数:{data['data']}\n日志信息:{dic}\n")
        print("\n----------------------------------------------------------------------------------------------\n")
        self.assertEqual(405, response.status_code)

    @json_data(r"D:\data\python_data\pythonProject\yunke\bot\include_Trusted_Bot.json")
    def test_include_Trusted_Bot(self, data):
        print(f"----------测试受信任的机器人(包含关系匹配),签名为:{data['title']}----------")
        trusted_bot_url = data_config.Trusted_Bot_url
        trusted_bot_head = {"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"}
        trusted_response = requests.post(url=trusted_bot_url, headers=trusted_bot_head,
                                         json=data_config.Trusted_Bot_data)
        if trusted_response.json()["code"] == 200:
            print("修改成功，响应码为:", trusted_response.status_code)
        else:
            print("修改失败,响应为:", trusted_response.json())
        response = requests.get(url=data_config.test_url, headers=data["header"])
        print(f"触发签名的值为：header={data['header']},触发规则返回的响应码：{response.status_code}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(response.text)
        print("re_info", re_info)
        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
            print(f"日志信息为：{dic}")
            with open(r"bot_logs", 'a+', encoding='utf-8') as f:
                f.write(
                    f"\n测试用例:测试受信任机器人(包含匹配),签名为:{data['title']}\n接口传参为:{data_config.Trusted_Bot_data}\n请求URL:{data_config.test_url}\n请求头：{data['header']}\n日志信息:{dic}\n")
        print("\n----------------------------------------------------------------------------------------------\n")
        self.assertEqual(405, response.status_code)

    @json_data(r"D:\data\python_data\pythonProject\yunke\bot\include_Untrusted_Bot.json")
    def test_include_Untrusted_Bot(self, data):
        print(f"----------测试不受信任的机器人(包含关系匹配),签名为:{data['title']}----------")
        untrusted_bot_url = data_config.Untrusted_url
        untrusted_bot_head = {"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"}
        untrusted_response = requests.post(url=untrusted_bot_url, headers=untrusted_bot_head,
                                           json=data_config.Untrusted_data)
        if untrusted_response.json()["code"] == 200:
            print("修改成功，响应码为:", untrusted_response.status_code)
        else:
            print("修改失败,响应为:", untrusted_response.json())
        response = requests.get(url=data_config.test_url, headers=data["header"], data=data["data"])
        print(f"触发签名的值为：header={data['header']},data={data['data']},触发规则返回的响应码：{response.status_code}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(response.text)
        print("re_info", re_info)
        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
            print(f"日志信息为：{dic}")
            with open(r"bot_logs", 'a+', encoding='utf-8') as f:
                f.write(
                    f"\n测试用例:测试不受信任机器人(包含匹配),签名为:{data['title']}\n接口传参为:{data_config.Untrusted_data}\n请求URL:{data_config.test_url}\n请求头：{data['header']}\n请求参数:{data['data']}\n日志信息:{dic}\n")
        print("\n----------------------------------------------------------------------------------------------\n")
        self.assertEqual(405, response.status_code)

    @json_data(r"D:\data\python_data\pythonProject\yunke\bot\include_Malicious_Bot.json")
    def test_include_Malicious_Bot(self, data):
        print(f"----------测试恶意的机器人(包含关系匹配),签名为:{data['title']}----------")
        malicious_bot_url = data_config.Malicious_Bot_url
        malicious_bot_head = {"open_api_token": global_parame.open_api_token, "Content-Type": "application/json"}
        malicious_response = requests.post(url=malicious_bot_url, headers=malicious_bot_head,
                                           json=data_config.Malicious_Bot_data)
        if malicious_response.json()["code"] == 200:
            print("修改成功，响应码为:", malicious_response.status_code)
        else:
            print("修改失败,响应为:", malicious_response.json())
        response = requests.post(url=data_config.test_url, headers=data["header"], data=data["data"])
        print(f"触发签名的值为：header={data['header']},data={data['data']},触发规则返回的响应码：{response.status_code}")
        re_info = re.compile(r'<span class="footer_ul_span">攻击类型：</span>.*?<span>(?P<type>.*?)</span>.*?<span '
                             r'class="footer_ul_span">策略ID：</span>.*?<span>(?P<type_id>.*?)</span>.*?<span '
                             r'class="footer_ul_span">本机IP：</span>.*?<span class="local_ip">(?P<local_ip>.*?).*?<span '
                             r'class="footer_ul_span">事件ID：</span>.*?<span class="logId">(?P<lod_id>.*?)</span>.*?',
                             re.S).finditer(response.text)
        print("re_info", re_info)
        for item in re_info:
            print(item.groupdict())
            dic = item.groupdict()
            print(f"日志信息为：{dic}")
            with open(r"bot_logs", 'a+', encoding='utf-8') as f:
                f.write(
                    f"\n测试用例:测试恶意的信任机器人(包含匹配),签名为:{data['title']}\n接口传参为:{data_config.Malicious_Bot_data}\n请求URL:{data_config.test_url}\n请求头：{data['header']}\n请求参数:{data['data']}\n日志信息:{dic}\n")
        print("\n----------------------------------------------------------------------------------------------\n")
        self.assertEqual(405, response.status_code)


if __name__ == '__main__':
    # 调试使用
    # unittest.main()
    # 返回当前工作目录
    path = os.path.dirname((os.path.realpath(__file__)))
    # 返回测试用例类的测试结果，加入工作目录路径以及文件名
    suite = unittest.defaultTestLoader.discover(path, pattern="test_bot_req.py")
    # TestRunner() 确定测试报告框架，将测试结果嵌套到框架中
    """             
        filename="report.html", 生成测试报告的html文件名称
        report_dir="./reports", 在工作文件的根目录下创建reports目录文件夹存放测试报告文件
        title='测试报告',             
        tester='测试员',             
        desc="XX项目测试生成的报告",             
        templates=1
    """
    runner = TestRunner(suite, title="bot反爬虫测试报告", tester="朱展鹏", desc="云科WAF防火墙", templates=3,report_dir=path)
    # 运行程序，生成报告
    runner.run()
