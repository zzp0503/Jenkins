import os

'''
    用户名参数、密码参数输入框做了字符限制的校验，所以自动化测试用例中不再测试字符长度限制的场景。
    响应码输入框和密码长度输入框对不符合规定的输入值写死了，不允许输入。所以写没必要写，而且也没办法断言。
'''
# 登录地址
login_url = "http://106.15.37.76:7778/"
# 用户名
login_username = "zhanpeng"
# 密码
login_password = "Sag123.."
# 测试文件名称
test_file_add_name = "\weak_pwd_add.json"
test_file_update_name = "\weak_pwd_update.json"
test_file_search_name = "\weak_pwd_search.json"
# 日志文件名称
log_file_name = "\weak_pwd_ui_log.txt"
# 工作目录
catalog = os.path.dirname(__file__)
# 测试文件路径
file_path_add = catalog + test_file_add_name
file_path_update = catalog + test_file_update_name
file_path_search = catalog + test_file_search_name
# 日志文件路径
log_file_path = catalog+log_file_name
