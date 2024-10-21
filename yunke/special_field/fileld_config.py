"""
    特殊字段逻辑匹配接口
"""
# 新增接口
add_url = "http://192.168.3.119:80/seraph-admin/admin-api/access_policy/special_field/add"

# 编辑接口
update_url = "http://192.168.3.119:80/seraph-admin/admin-api/access_policy/special_field/update"

# 列表接口
list_url = "http://192.168.3.119:80/seraph-admin/admin-api/access_policy/special_field/list"

# 删除接口
delete_url = "http://192.168.3.119:80/seraph-admin/admin-api/access_policy/special_field/delete"
# 详情接口
get_url = "http://192.168.3.119:80/seraph-admin/admin-api/access_policy/special_field/get"
"""
    请求头
"""
filed_head = {"open_api_token": "5c778ce7-787f-4107-b747-d7f665e61ab3", "Content-Type": "application/json"}

"""
    匹配字段："key"
        1：URI
        2：Query
        3：GET参数
        4：Method
        5：Host
        6：Cookie参数
        7：User Agent
        8：Referrer
        9：Content-Type
        10：Content-Length
        11：用户IP
        12：X-Forwarded-For
        13：Origin
        14：Accept-Language
        15：Authorization
        16：HTTP请求头
        17：HTTP请求头长度
        18：POST参数
        19：完整Body
        20：上传的文件名
        21：HTTP状态码
        22：HTTP响应头
        23：响应内容
    匹配方式："condition"
        1:	包含
        2:	不包含
        3:	完全匹配
        4:	不完全匹配
        5:	正则匹配
        6:	正则不匹配
        7:	小于
        8:	小于等于
        9:	等于
        10:	不等于
        11:	大于
        12:	大于等于
        13:	等于多值之一
        14:	不等于任一值
"""
# 应用id
app_id = 53
# 规则id
id = ""
