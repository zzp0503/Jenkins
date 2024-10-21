from yunke import global_parame

# 自定义请求方式编辑接口
request_type_update_url = (f"http://{global_parame.host}:{global_parame.port}/seraph-admin/admin-api"
                           f"/custom_request_type/update")

# 放行所有请求
request_type_update_data_Release = {
    "app_id": global_parame.app_id,
    "status": True,
    "types": ["ACL", "BCOPY", "BDELETE", "BMOVE", "BPROPFIND", "BPROPPATCH", "CHECKIN", "CHECKOUT", "CONNECT", "COPY",
              "DELETE", "GET", "HEAD", "LINK", "LOCK", "MERGE", "MKCOL", "MKWORKSPACE", "MOVE", "NOTIFY", "OPTIONS",
              "PATCH", "POLL", "POST", "PROPFIND", "PROPPATCH", "PUT", "REPORT", "RPC_IN_DATA", "RPC_OUT_DATA",
              "SEARCH", "SUBSCRIBE", "TRACE", "TRACK", "UNLINK", "UNLOCK", "UNSUBSCRIBE", "VERSION_CONTROL",
              "X-MS-ENUMATTS"],
    "action": 400
}

# 阻断所有请求
request_type_update_data_block = {
    "app_id": global_parame.app_id,
    "status": True,
    "types": [],
    "action": 400
}
# 阻断所有请求——关闭状态
request_type_update_data_close = {
    "app_id": global_parame.app_id,
    "status": False,
    "types": [],
    "action": 400
}
# 重复开启
request_type_update_data_open = {
    "app_id": global_parame.app_id,
    "status": True,
    "types": [],
    "action": 400
}

"""
    请求头
"""
