import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import element_info, method, data_config
from unittestreport import ddt, json_data, TestRunner
from selenium.webdriver.support.select import Select


@ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 判断日志文件是否存在，如果存在则删除
        if os.path.exists(data_config.log_file_path):
            os.remove(data_config.log_file_path)
            print("删除日志文件成功，开始测试。\n------------------------------------------------------------")
        else:
            pass
        # 进入登录页面
        method.get(data=data_config.login_url)
        # 放大窗口
        method.maximize()
        time.sleep(1)
        # 隐式等待
        method.implicitly_wait(10)
        # 输入账号
        method.send_key(element=element_info.Login_element.username, data=data_config.login_username)
        # 输入密码
        method.send_key(element=element_info.Login_element.password, data=data_config.login_password)
        # 点击登录按钮
        method.chick(element=element_info.Login_element.login_button)
        time.sleep(2)
        # 应用高级防御设置页面
        method.chick(element=element_info.Weak_pwd.defense)
        # 点击弱口令防御
        time.sleep(2)
        method.chick(element=element_info.Weak_pwd.weak)

    @classmethod
    def tearDownClass(cls) -> None:
        method.close()

    @json_data(data_config.file_path_add)
    def test_add(self, data):
        # 点击添加,进入添加页面
        time.sleep(3)
        method.chick(element=element_info.Weak_pwd.add)
        time.sleep(2)
        # 输入用户名参数
        method.send_key(element=element_info.Weak_pwd.username,
                        data=data["username"], element_type=2, index=0)
        # 输入密码参数
        method.send_key(element=element_info.Weak_pwd.password,
                        data=data["password"], element_type=2, index=1)
        # 点击加密方式
        if data["encrypt_type"] == 0:
            # 选择字母
            if data["letter"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.letter, index=0)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=0))

            else:
                pass
            # 选择大写字母
            if data["upper"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.upper, index=1)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=1))
            else:
                pass
            # 选择小写字母
            if data["lower"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.lower, index=2)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=2))
            else:
                pass
            # 选择数字
            if data["num"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.num, index=3)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=3))
            else:
                pass
            # 选择特殊符号
            if data["punctuation"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.punctuation, index=4)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=4))
            else:
                pass
            # 选择账号与密码相同
            if data["name_pwd_equal"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.name_pwd_equal, index=0)
            else:
                pass
            # 选择连续字符检测
            if data["continuous_char"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.continuous_char, index=1)
            else:
                pass
            # 输入响应码
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入密码长度
            method.send_key(element=element_info.Weak_pwd.len, data=data["len"])
            # 输入名称
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])

        elif data["encrypt_type"] == 1:
            time.sleep(1)
            method.script_chick(element=element_info.Weak_pwd.encrypt_type)
            time.sleep(1)
            method.chick(element=element_info.Weak_pwd.encrypt_type_1)
            # 选择字母
            if data["letter"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.letter, index=0)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=0))

            else:
                pass
            # 选择大写字母
            if data["upper"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.upper, index=1)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=1))
            else:
                pass
            # 选择小写字母
            if data["lower"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.lower, index=2)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=2))
            else:
                pass
            # 选择数字
            if data["num"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.num, index=3)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=3))
            else:
                pass
            # 选择特殊符号
            if data["punctuation"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.punctuation, index=4)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=4))
            else:
                pass
            # 选择账号与密码相同
            if data["name_pwd_equal"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.name_pwd_equal, index=0)
            else:
                pass
            # 选择连续字符检测
            if data["continuous_char"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.continuous_char, index=1)
            else:
                pass
            # 输入响应码
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入密码长度
            method.send_key(element=element_info.Weak_pwd.len, data=data["len"])
            # 输入名称
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
        elif data["encrypt_type"] == 2:
            time.sleep(1)
            method.script_chick(element=element_info.Weak_pwd.encrypt_type)
            time.sleep(1)
            method.chick(element=element_info.Weak_pwd.encrypt_type_2)
            # 选择字母
            if data["letter"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.letter, index=0)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=0))

            else:
                pass
            # 选择大写字母
            if data["upper"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.upper, index=1)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=1))
            else:
                pass
            # 选择小写字母
            if data["lower"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.lower, index=2)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=2))
            else:
                pass
            # 选择数字
            if data["num"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.num, index=3)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=3))
            else:
                pass
            # 选择特殊符号
            if data["punctuation"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.punctuation, index=4)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=4))
            else:
                pass
            # 选择账号与密码相同
            if data["name_pwd_equal"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.name_pwd_equal, index=0)
            else:
                pass
            # 选择连续字符检测
            if data["continuous_char"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.continuous_char, index=1)
            else:
                pass
            # 输入响应码
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入密码长度
            method.send_key(element=element_info.Weak_pwd.len, data=data["len"])
            # 输入名称
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])

        elif data["encrypt_type"] == 3:
            time.sleep(2)
            method.script_chick(element=element_info.Weak_pwd.encrypt_type)
            time.sleep(2)
            # 点击
            method.script_chick(element=element_info.Weak_pwd.encrypt_type_3)
            # 输入响应码
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入名称
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])

    @json_data(file_path=data_config.file_path_update)
    def test_update(self, data):
        # 点击编辑按钮
        method.chick(element_type=2, element=element_info.Weak_pwd.update, index=0)
        # 修改用户名
        time.sleep(1)
        method.clear(element=element_info.Weak_pwd.username, element_type=2, index=0)
        method.chick(element=element_info.Weak_pwd.username, element_type=2, index=0)
        method.send_key(element=element_info.Weak_pwd.username,
                        data=data["username"], element_type=2, index=0)
        # 修改密码
        time.sleep(1)
        method.clear(element=element_info.Weak_pwd.username, element_type=2, index=1)
        method.chick(element=element_info.Weak_pwd.username, element_type=2, index=1)
        method.send_key(element=element_info.Weak_pwd.password,
                        data=data["password"], element_type=2, index=1)
        # 点击加密方式
        if data["encrypt_type"] == 0:
            # 选择字母
            if data["letter"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.letter, index=0)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=0))

            else:
                pass
            # 选择大写字母
            if data["upper"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.upper, index=1)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=1))
            else:
                pass
            # 选择小写字母
            if data["lower"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.lower, index=2)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=2))
            else:
                pass
            # 选择数字
            if data["num"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.num, index=3)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=3))
            else:
                pass
            # 选择特殊符号
            if data["punctuation"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.punctuation, index=4)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=4))
            else:
                pass
            # 选择账号与密码相同
            if data["name_pwd_equal"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.name_pwd_equal, index=0)
            else:
                pass
            # 选择连续字符检测
            if data["continuous_char"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.continuous_char, index=1)
            else:
                pass
            # 输入响应码
            method.clear(element=element_info.Weak_pwd.status_code, element_type=2, index=2)
            method.chick(element=element_info.Weak_pwd.status_code, element_type=2, index=2)
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.clear(element=element_info.Weak_pwd.identify_key_word, element_type=2, index=3)
            method.chick(element=element_info.Weak_pwd.identify_key_word, element_type=2, index=3)
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.clear(element=element_info.Weak_pwd.url)
            method.chick(element=element_info.Weak_pwd.url)
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入密码长度
            method.clear(element=element_info.Weak_pwd.len)
            method.send_key(element=element_info.Weak_pwd.len, data=data["len"])
            # 输入名称
            method.clear(element=element_info.Weak_pwd.name, element_type=2, index=4)
            method.chick(element=element_info.Weak_pwd.name, element_type=2, index=4)
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.script_chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.script_chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])

        elif data["encrypt_type"] == 1:
            time.sleep(1)
            method.script_chick(element=element_info.Weak_pwd.encrypt_type)
            time.sleep(1)
            method.chick(element=element_info.Weak_pwd.encrypt_type_1)
            # 选择字母
            if data["letter"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.letter, index=0)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=0))

            else:
                pass
            # 选择大写字母
            if data["upper"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.upper, index=1)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=1))
            else:
                pass
            # 选择小写字母
            if data["lower"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.lower, index=2)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=2))
            else:
                pass
            # 选择数字
            if data["num"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.num, index=3)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=3))
            else:
                pass
            # 选择特殊符号
            if data["punctuation"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.punctuation, index=4)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=4))
            else:
                pass
            # 选择账号与密码相同
            if data["name_pwd_equal"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.name_pwd_equal, index=0)
            else:
                pass
            # 选择连续字符检测
            if data["continuous_char"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.continuous_char, index=1)
            else:
                pass
            # 输入响应码
            method.clear(element=element_info.Weak_pwd.status_code, element_type=2, index=2)
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.clear(element=element_info.Weak_pwd.identify_key_word, element_type=2, index=3)
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.clear(element=element_info.Weak_pwd.url)
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入密码长度
            method.clear(element=element_info.Weak_pwd.len)
            method.send_key(element=element_info.Weak_pwd.len, data=data["len"])
            # 输入名称
            method.clear(element=element_info.Weak_pwd.name, element_type=2, index=4)
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
        elif data["encrypt_type"] == 2:
            time.sleep(1)
            method.script_chick(element=element_info.Weak_pwd.encrypt_type)
            time.sleep(1)
            method.chick(element=element_info.Weak_pwd.encrypt_type_2)
            # 选择字母
            if data["letter"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.letter, index=0)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=0))

            else:
                pass
            # 选择大写字母
            if data["upper"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.upper, index=1)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=1))
            else:
                pass
            # 选择小写字母
            if data["lower"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.lower, index=2)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=2))
            else:
                pass
            # 选择数字
            if data["num"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.num, index=3)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=3))
            else:
                pass
            # 选择特殊符号
            if data["punctuation"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.punctuation, index=4)
                print(method.text(element_type=2, element=element_info.Weak_pwd.letter, index=4))
            else:
                pass
            # 选择账号与密码相同
            if data["name_pwd_equal"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.name_pwd_equal, index=0)
            else:
                pass
            # 选择连续字符检测
            if data["continuous_char"] == True:
                time.sleep(1)
                method.chick(element_type=2, element=element_info.Weak_pwd.continuous_char, index=1)
            else:
                pass
            # 输入响应码
            method.clear(element=element_info.Weak_pwd.status_code, element_type=2, index=2)
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.clear(element=element_info.Weak_pwd.identify_key_word, element_type=2, index=3)
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.clear(element=element_info.Weak_pwd.url)
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入密码长度
            method.clear(element=element_info.Weak_pwd.len)
            method.send_key(element=element_info.Weak_pwd.len, data=data["len"])
            # 输入名称
            method.clear(element=element_info.Weak_pwd.name, element_type=2, index=4)
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])

        elif data["encrypt_type"] == 3:
            time.sleep(2)
            method.script_chick(element=element_info.Weak_pwd.encrypt_type)
            time.sleep(2)
            # 点击
            method.script_chick(element=element_info.Weak_pwd.update_encrypt_type_3)
            # 输入响应码
            method.clear(element=element_info.Weak_pwd.status_code, element_type=2, index=2)
            method.send_key(element=element_info.Weak_pwd.status_code, data=data["status_code"], element_type=2,
                            index=2)
            # 输入特征字符
            method.clear(element=element_info.Weak_pwd.identify_key_word, element_type=2, index=3)
            method.send_key(element=element_info.Weak_pwd.identify_key_word, data=data["identify_key_word"],
                            element_type=2, index=3)
            # 输入URL
            method.clear(element=element_info.Weak_pwd.url)
            method.send_key(element=element_info.Weak_pwd.url, data=data["url"])
            # 输入名称
            method.clear(element=element_info.Weak_pwd.name, element_type=2, index=4)
            method.send_key(element=element_info.Weak_pwd.name, data=data["name"], element_type=2, index=4)
            # 点击确定
            if data["expect"] == "操作成功":
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                # 截图
                method.screenshot(title=data["title"], path=data_config.catalog)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.success)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])
            else:
                time.sleep(2)
                method.chick(element=element_info.Weak_pwd.confirm)
                time.sleep(1)
                method.chick(element=element_info.Weak_pwd.close)
                # 打印结果
                a = method.text(element=element_info.Weak_pwd.fail)
                print(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                with open(file=data_config.log_file_path, mode='a+', encoding='utf-8') as f:
                    f.write(f"\n测试标题：{data['title']}，\n预期结果为：{data['expect']}，实际结果为：{a}\n")
                    # 断言，查看新创建的规则是否成功
                    self.assertEqual(a, data["expect"])

    # @json_data(file_path=data_config.test_file_search_name)
    # def test_search(self,data):
    #     # 点击搜索框
    #     method.chick(element=element_info.Weak_pwd.search)
    #     # 选择检索条件
    #     if data["search_type"]=="url":
    #         method.chick(element_type=2,index=0,element=element_info.Weak_pwd.search_url)
    #         if data["relation"] == "等于":
    #             method.chick(element=element_info.Weak_pwd.search_url_equal)
    #             # 输入内容
    #             method.send_key(element=element_info.Weak_pwd.search_content,data=data["search_content"])
    #
    #             self.assertEqual()
    #         else:
    #             method.chick(element=element_info.Weak_pwd.search_url_fuzzy)
    #             # 输入内容
    #
    #     elif data["search_type"]=="name":
    #         method.chick(element_type=2, index=1, element=element_info.Weak_pwd.search_url)
    #         method.chick(element=element_info.Weak_pwd.search_url_fuzzy)


if __name__ == '__main__':
    # unittest.main()
    path = os.path.dirname((os.path.realpath(__file__)))
    # 返回测试用例类的测试结果，加入工作目录路径以及文件名
    suite = unittest.defaultTestLoader.discover(path, pattern="test_weak_pwd.py")
    # TestRunner() 确定测试报告框架，将测试结果嵌套到框架中
    """
        filename="report.html", 生成测试报告的html文件名称
        report_dir="./reports", 在工作文件的根目录下创建reports目录文件夹存放测试报告文件
        title='测试报告',
        tester='测试员',
        desc="XX项目测试生成的报告",
        templates=1
    """
    runner = TestRunner(suite, title="弱口令测试报告", tester="朱展鹏", desc="云科WAF防火墙", templates=3,
                        report_dir=path)
    # 运行程序，生成报告
    runner.run()
