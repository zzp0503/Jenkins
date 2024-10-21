import os
import time
import unittest
import requests, fileld_config
from unittestreport import ddt, TestRunner, json_data


@ddt
class Test_Special_field(unittest.TestCase):
    """
        新增接口参数值测试
    """

    @json_data('field.json')
    def test_add_rule(self, data):
        # 新增规则
        add_data = {
            "app_id": fileld_config.app_id,
            "name": data["field_data"]["name"],
            "description": data["field_data"]["description"],
            "action": data["field_data"]["action"],
            "condition_relation": data["field_data"]["condition_relation"],
            "condition": data["field_data"]["condition"],
            "status": data["field_data"]["status"]
        }
        add_response = requests.post(url=fileld_config.add_url, headers=fileld_config.filed_head, json=add_data)
        # 新增规则成功，获取新增规则的id
        if add_response.status_code == 200:
            print(f"新增规则成功，响应结果为：{add_response.json()},\n规则id为：{add_response.json()['data']['id']}")
            time.sleep(0.5)
            rule_id = {
                "id": add_response.json()['data']['id']
            }
            # 删除新增的规则
            delete_response = requests.post(url=fileld_config.delete_url, headers=fileld_config.filed_head,
                                            json=rule_id)
            # 删除后进行查询
            get_response = requests.post(url=fileld_config.get_url, headers=fileld_config.filed_head, json=rule_id)
            if get_response.json()["message"] == "数据不存在":
                print(f"删除成功")
            else:
                print("删除失败")
            self.assertEqual(data["expect"], add_response.json()["code"])

        else:
            print(f"新增规则失败，响应结果为：{add_response.json()}")


if __name__ == '__main__':
    # unittest.main()
    # 返回当前工作目录
    path = os.getcwd()
    # 返回测试用例类的测试结果，加入工作目录路径以及文件名
    suite = unittest.defaultTestLoader.discover(path, pattern="test_field.py")
    # TestRunner() 确定测试报告框架，将测试结果嵌套到框架中
    """             
        filename="report.html", 生成测试报告的html文件名称
        report_dir="./reports", 在工作文件的根目录下创建reports目录文件夹存放测试报告文件
        title='测试报告',             
        tester='测试员',             
        desc="XX项目测试生成的报告",             
        templates=1
    """
    runner = TestRunner(suite, title="字段逻辑匹配测试报告", tester="朱展鹏", desc="云科WAF防火墙", templates=3)
    # 运行程序，生成报告
    runner.run()
