from yunke import global_parame

# 测试URL路径
test_url = global_parame.proxy_ip
"--------------------------------------------------------------------------------------------------------------------"
'''
    正向——Trusted_Bot 接口
'''
Trusted_Bot_url = f"{global_parame.admin_ip}/seraph-admin/admin-api/bot_policy/update"
Trusted_Bot_data = {
    "app_id": global_parame.app_id,
    "action_settings": {
        "trusted_bot": 100,
        "untrusted_bot": 400,
        "suspicious_browser": 400,
        "malicious_bot": 400,
        "unknown": 400
    },
    "dos": {
        "interval_milliseconds": 1000,
        "is_enabled": False,
        "max_count": 10,
        "action": 100,
        "freeze_time": 2
    },
    "browsers": {
        "verification": 1,
        "type": 1,
        "domains": []
    },
    "exception": [],
    "status": True
}

"--------------------------------------------------------------------------------------------------------------------"
'''
    正向——Untrusted_Bot 接口
'''
Untrusted_url = f"{global_parame.admin_ip}/seraph-admin/admin-api/bot_policy/update"
Untrusted_data = {
    "app_id": global_parame.app_id,
    "action_settings": {
        "trusted_bot": 400,
        "untrusted_bot": 100,
        "suspicious_browser": 400,
        "malicious_bot": 400,
        "unknown": 400
    },
    "dos": {
        "interval_milliseconds": 1000,
        "is_enabled": False,
        "max_count": 10,
        "action": 100,
        "freeze_time": 2
    },
    "browsers": {
        "verification": 1,
        "type": 1,
        "domains": []
    },
    "exception": [],
    "status": True
}

"--------------------------------------------------------------------------------------------------------------------"
'''
    正向——Malicious_Bot 接口
'''
Malicious_Bot_url = f"{global_parame.admin_ip}/seraph-admin/admin-api/bot_policy/update"
Malicious_Bot_data = {
    "app_id": global_parame.app_id,
    "action_settings": {
        "trusted_bot": 400,
        "untrusted_bot": 400,
        "suspicious_browser": 400,
        "malicious_bot": 100,
        "unknown": 400
    },
    "dos": {
        "interval_milliseconds": 1000,
        "is_enabled": False,
        "max_count": 10,
        "action": 100,
        "freeze_time": 2
    },
    "browsers": {
        "verification": 1,
        "type": 1,
        "domains": []
    },
    "exception": [],
    "status": True
}

"--------------------------------------------------------------------------------------------------------------------"
'''
    反向——Trusted_Bot 接口
'''
Trusted_Bot_url_opposite = f"{global_parame.admin_ip}/seraph-admin/admin-api/bot_policy/update"
Trusted_Bot_data_opposite = {
    "app_id": global_parame.app_id,
    "action_settings": {
        "trusted_bot": 400,
        "untrusted_bot": 100,
        "suspicious_browser": 100,
        "malicious_bot": 100,
        "unknown": 100
    },
    "dos": {
        "interval_milliseconds": 1000,
        "is_enabled": False,
        "max_count": 10,
        "action": 100,
        "freeze_time": 2
    },
    "browsers": {
        "verification": 1,
        "type": 1,
        "domains": []
    },
    "exception": [],
    "status": True
}

"--------------------------------------------------------------------------------------------------------------------"
'''
    反向——Untrusted_Bot 接口
'''
Untrusted_url_opposite = f"{global_parame.admin_ip}/seraph-admin/admin-api/bot_policy/update"
Untrusted_data_opposite = {
    "app_id": global_parame.app_id,
    "action_settings": {
        "trusted_bot": 100,
        "untrusted_bot": 400,
        "suspicious_browser": 100,
        "malicious_bot": 100,
        "unknown": 100
    },
    "dos": {
        "interval_milliseconds": 1000,
        "is_enabled": False,
        "max_count": 10,
        "action": 100,
        "freeze_time": 2
    },
    "browsers": {
        "verification": 1,
        "type": 1,
        "domains": []
    },
    "exception": [],
    "status": True
}

"--------------------------------------------------------------------------------------------------------------------"
'''
    反向——Malicious_Bot 接口
'''
Malicious_Bot_url_opposite = f"{global_parame.admin_ip}/seraph-admin/admin-api/bot_policy/update"
Malicious_Bot_data_opposite = {
    "app_id": global_parame.app_id,
    "action_settings": {
        "trusted_bot": 100,
        "untrusted_bot": 100,
        "suspicious_browser": 100,
        "malicious_bot": 400,
        "unknown": 100
    },
    "dos": {
        "interval_milliseconds": 1000,
        "is_enabled": False,
        "max_count": 10,
        "action": 100,
        "freeze_time": 2
    },
    "browsers": {
        "verification": 1,
        "type": 1,
        "domains": []

    },
    "exception": [],
    "status": True
}
