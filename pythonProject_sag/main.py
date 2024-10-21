import json
import random

from fastapi import FastAPI, Header, Body, Request, File
import uvicorn
from pydantic import BaseModel
from typing import Union


class Item1(BaseModel):
    username: str
    password: str
    username2: str
    password2: str


app = FastAPI()


# 弱口令测试
@app.post("/weak_pwd1")
def weak_pwd(data: Item1):
    body = {"code": 200, "login_msg": "success", "login_info": data}
    return body


@app.get("/weak_pwd2")
def weak_pwd(username, password):
    body = {"code": 200, "login_msg": "success", "login_info": {"username": username, "password": password}}
    return body


# 防敏感休息泄露测试
class Info(BaseModel):
    id_card: str
    phone: str
    bank_card: str
    mailbox: str
    keyword: str


@app.post("/id_card_info1")
def id_card1(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data.id_card}
    return body


@app.post("/id_card_info2")
def id_card2(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data.id_card}
    return body


@app.post("/phone_info")
def phone_info(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data.phone}
    return body


@app.post("/bank_card")
def bank_card(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data.bank_card}
    return body


@app.post("/mailbox_info")
def mailbox_info(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data.mailbox}
    return body


@app.post("/more_data")
def more_data(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data}
    return body


@app.post("/more_info")
def more_data(data: Info):
    more_info = {
        "敏感数据1": "14230320010503363X",
        "敏感数据2": "14230320010503363X",
        "敏感数据3": "14230320010503363X",
        "敏感数据4": "14230320010503363X",
        "敏感数据5": "14230320010503363X",
        "敏感数据6": "14230320010503363X",
        "敏感数据7": "14230320010503363X",
        "敏感数据8": "14230320010503363X",
        "敏感数据9": "14230320010503363X",
        "敏感数据10": "14230320010503363X",
        "敏感数据11": "14230320010503363X",
        "敏感数据12": "14230320010503363X",
        "敏感数据13": "14230320010503363X",
        "敏感数据14": "14230320010503363X",
        "敏感数据15": "14230320010503363X",
        "敏感数据16": "14230320010503363X",
        "敏感数据17": "14230320010503363X",
        "敏感数据18": "14230320010503363X",
        "敏感数据19": "14230320010503363X",
        "敏感数据20": "14230320010503363X"
    }
    body = {"code": 200, "msg": "success", "msg_info": more_info}
    return body


@app.post("/keyword")
def keyword(data: Info):
    body = {"code": 200, "msg": "success", "msg_info": data.keyword}
    return body


@app.post("/more_keyword")
def keyword(data: Info):
    keyword_info = {
        "关键字1": "关键字@keyword",
        "关键字2": "Sag//",
        "关键字3": 12345
    }
    body = {"code": 200, "msg": "success", "msg_info": keyword_info}
    return body


# 一键封海外IP测试
@app.get("/foreign_IP")
def foreign_IP(X_REAL_IP: Union[str, None] = Header(default=None)):
    return {"code": 200, "X_REAL_IP:": X_REAL_IP}


# cc防护测试
@app.get("/user_agent1")
def user_agent1(User_Agent: Union[str, None] = Header(default=None)):
    return {"code": 200, "User_Agent:": User_Agent}


@app.get("/user_agent2")
def user_agent2(User_Agent: Union[str, None] = Header(default=None)):
    return {"code": 200, "User_Agent:": User_Agent}


@app.get("/cookie1")
def cookie1(Cookie: Union[str, None] = Header(default=None)):
    return {"code": 200, "Cookie:": Cookie}


@app.get("/cookie2")
def cookie2(Cookie: Union[str, None] = Header(default=None)):
    return {"code": 200, "Cookie:": Cookie}


@app.get("/url_path")
def url_path(a):
    return {"code": 200, "a:": a}


# url黑白名单
# web shell文件上传
@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# url令牌
@app.get("/url_seraph_csrf")
def seraph_csrf(seraph_csrf):
    return {"code": 200, "seraph_csrf:": seraph_csrf}


# 多参数
@app.get("/more_param")
def more_param(a, b, c, d):
    return {"code": 200, "参数a:": a, "参数b": b, "参数c": c, "参数d": d}


'''
    自定义请求方式
'''


class Method(BaseModel):
    method: str

    # get请求


@app.get("/get_method")
def get_method(a):
    return {"code": 200, "msg": a, "method": "get"}

    # post请求


@app.post("/post_method")
def post_method(data: Method):
    body = {"code": 200, "method": data}
    return body


@app.head("/head_method")
def head_method(data: Method):
    body = {"code": 200, "method": data}
    return body


@app.put("/put_method")
def put_method(data: Method):
    body = {"code": 200, "method": data}
    return body


@app.delete("/delete_method")
def delete_method(data: Method):
    body = {"code": 200, "method": data}
    return body


@app.options("/options_method")
def options_method(data: Method):
    body = {"code": 200, "method": data}
    return body


@app.trace("/trace_method")
def trace_method(data: Method):
    body = {"code": 200, "method": data}
    return body


@app.patch("/patch_method")
def patch_method(data: Method):
    body = {"code": 200, "method": data}
    return body


class Data_qaq(BaseModel):
    wsqmgxx: str = None
    gpfw: str = None


class Passport(BaseModel):
    passport: str = None
    mailbox: str = None
    idcard: str = None
    ipaddr: str = None
    creditcode: str = None
    iphone: str = None
    iphone_and_mailbox: str = None
    mailbox_and_creditcode: str = None
    mailbox_and_ipaddr: str = None
    mailbox_and_xyk: str = None
    mailbox_and_idcard: str = None  # 1111
    iphone_and_creditcode: str = None
    iphone_and_ipaddr: str = None
    iphone_and_xyk: str = None
    iphone_and_idcard: str = None
    creditcode_and_ipaddr: str = None
    creditcode_and_xyk: str = None
    creditcode_and_idcard: str = None
    xyk_and_ipaddr: str = None
    idcard_and_ipaddr: str = None
    idcard_and_xyk: str = None  # 11
    HKandMacau: str = None
    car: str = None
    mlxy: str = None
    xyk: str = None
    ssn: str = None
    address: str = None
    yyzz: str = None
    v6: str = None
    car_num: str = None
    mac: str = None
    zjxy: str = None
    IMEI: str = None
    linux_password: str = None
    linux_shadow: str = None
    pem: str = None
    credit_card: str = None
    ml: str = None
    Tax_number: str = None
    institution_code: str = None
    iphone_and_creditcod: str = None


class Data_qaq(BaseModel):
    xx: str = None
    yy: str = None


# 记录报错
@app.post("/api/error")
async def test(data: Data_qaq):
    if data.xx is not None:
        body = {'return_code': '200', 'return_info': {"System.Data.OleDb.OleDbException", "[SQL Server]"}}
        return body
    else:
        pass


# 异步终端访问
@app.get("/py")
def py(user_agent: Union[str, None] = Header(default=None)):
    """ 异步终端访问 """
    return {"code": 200,
            "content_disposition": user_agent,
            "content_disposition1": user_agent,
            "content_disposition2": user_agent,
            "content_disposition3": user_agent,
            "msg": "export_succeed"

            }


@app.post("/api/passport")
async def passport(data: Passport):
    if data.passport is not None:
        body = {"msg1": ["E05260892"],
                "msg2": ["G52603939"],
                "msg3": ["E04580757"],
                "msg4": ["E05260892"],
                "msg5": ["G52603939"],
                "msg6": ["E04580757"],
                "msg7": ["E05260892"],
                "msg8": ["G52603939"],
                "msg9": ["E04580757"],
                "msg10": ["E04580757"]
                }
        return body
    else:
        pass


@app.post("/api/mailbox")
async def mailbox(data: Passport):
    if data.mailbox is not None:
        body = {"msg1": ["13613415737@163.com"],
                "msg2": ["1370342627@qq.com"],
                "msg3": ["dongyan.wang@antiratech.com.cn"],
                "msg4": ["13613415737@163.com"],
                "msg5": ["1370342627@qq.com"],
                "msg6": ["dongyan.wang@antiratech.com.cn"],
                "msg7": ["13613415737@163.com"],
                "msg8": ["1370342627@qq.com"],
                "msg9": ["dongyan.wang@antiratech.com.cn"],
                "msg10": ["dongyan.wang@antiratech.com.cn"],
                }
        return body
    else:
        pass


@app.post("/api/idcard")
async def idcard(data: Passport):
    if data.idcard is not None:
        body = {"msg1": ["130725196703046219"],
                "msg2": ["130725196703048513"],
                "msg3": ["130725196703048513"],
                "msg4": ["142303199905033638"],
                "msg5": ["14230320010503363X"],
                "msg6": ["142303199905033634"],
                "msg7": ["142303199905033633"],
                "msg8": ["142303199905033634"],
                "msg9": ["142303199905033631"],
                "msg10": ["142303199905033631"]}
        return body
    else:
        pass


@app.post("/api/ipaddr")
async def ipaddr(data: Passport):
    if data.ipaddr is not None:
        body = {"msg1": ["192.168.3.32"],
                "msg2": ["192.168.3.32"],
                "msg3": ["192.168.3.32"],
                "msg4": ["192.168.3.32"],
                "msg5": ["192.168.3.32"],
                "msg6": ["192.168.3.32"],
                "msg7": ["192.168.3.32"],
                "msg8": ["192.168.3.32"],
                "msg9": ["192.168.3.32"],
                "msg10": ["192.168.3.32"]}
        return body
    else:
        pass


@app.post("/api/creditcode")
async def creditcode(data: Passport):
    if data.creditcode is not None:
        body = {"msg1": ["91310109MA1G5KN01M"],
                "msg2": ["91310109MA1G5KN01M"],
                "msg3": ["91310109MA1G5KN01M"],
                "msg4": ["91310109MA1G5KN01M"],
                "msg5": ["91310109MA1G5KN01M"],
                "msg6": ["91310109MA1G5KN01M"],
                "msg7": ["91310109MA1G5KN01M"],
                "msg8": ["91310109MA1G5KN01M"],
                "msg9": ["91310109MA1G5KN01M"],
                "msg10": ["91310109MA1G5KN01M"]}
        return body
    else:
        pass


@app.post("/api/iphone")
async def iphone(data: Passport):
    if data.iphone is not None:
        body = {"msg1": ["13934015806"],
                "msg2": ["13934015806"],
                "msg3": ["13934015806"],
                "msg4": ["13934015806"],
                "msg5": ["13934015806"],
                "msg6": ["13934015806"],
                "msg7": ["13934015806"],
                "msg8": ["13934015806"],
                "msg9": ["13934015806"],
                "msg10": ["13934015806"]}
        return body
    else:
        pass


@app.post("/api/iphone_and_mailbox")
async def iphone_and_mailbox(data: Passport):
    if data.iphone_and_mailbox is not None:
        body = {"msg1": ["13934015806"],
                "msg2": ["13934015806"],
                "msg3": ["13934015806"],
                "msg4": ["13934015806"],
                "msg5": ["13934015806"],
                "msg6": ["13934015806"],
                "msg7": ["13934015806"],
                "msg8": ["13934015806"],
                "msg9": ["13934015806"],
                "msg10": ["13934015806"],
                "msg11": ["13613415737@163.com"],
                "msg12": ["13613415737@163.com"],
                "msg13": ["13613415737@163.com"],
                "msg14": ["13613415737@163.com"],
                "msg15": ["13613415737@163.com"],
                "msg16": ["13613415737@163.com"],
                "msg17": ["13613415737@163.com"],
                "msg18": ["13613415737@163.com"],
                "msg19": ["13613415737@163.com"],
                "msg20": ["13613415737@163.com"]
                }
        return body
    else:
        pass


# mailbox_and_creditcode
@app.post("/api/mailbox_and_creditcode")
async def mailbox_and_creditcode(data: Passport):
    if data.mailbox_and_creditcode is not None:
        body = {"msg1": ["13613415737@163.com"],
                "msg2": ["13613415737@163.com"],
                "msg3": ["13613415737@163.com"],
                "msg4": ["13613415737@163.com"],
                "msg5": ["13613415737@163.com"],
                "msg6": ["13613415737@163.com"],
                "msg7": ["13613415737@163.com"],
                "msg8": ["13613415737@163.com"],
                "msg9": ["13613415737@163.com"],
                "msg10": ["13613415737@163.com"],
                "msg11": ["91310109MA1G5KN01M"],
                "msg12": ["91310109MA1G5KN01M"],
                "msg13": ["91310109MA1G5KN01M"],
                "msg14": ["91310109MA1G5KN01M"],
                "msg15": ["91310109MA1G5KN01M"],
                "msg16": ["91310109MA1G5KN01M"],
                "msg17": ["91310109MA1G5KN01M"],
                "msg18": ["91310109MA1G5KN01M"],
                "msg19": ["91310109MA1G5KN01M"],
                "msg20": ["91310109MA1G5KN01M"]
                }
        return body
    else:
        pass


# mailbox_and_ipaddr

@app.post("/api/mailbox_and_ipaddr")
async def mailbox_and_ipaddr(data: Passport):
    if data.mailbox_and_ipaddr is not None:
        body = {"msg1": ["13613415737@163.com"],
                "msg2": ["13613415737@163.com"],
                "msg3": ["13613415737@163.com"],
                "msg4": ["13613415737@163.com"],
                "msg5": ["13613415737@163.com"],
                "msg6": ["13613415737@163.com"],
                "msg7": ["13613415737@163.com"],
                "msg8": ["13613415737@163.com"],
                "msg9": ["13613415737@163.com"],
                "msg10": ["13613415737@163.com"],
                "msg11": ["192.168.3.32"],
                "msg12": ["192.168.3.32"],
                "msg13": ["192.168.3.32"],
                "msg14": ["192.168.3.32"],
                "msg15": ["192.168.3.32"],
                "msg16": ["192.168.3.32"],
                "msg17": ["192.168.3.32"],
                "msg18": ["192.168.3.32"],
                "msg19": ["192.168.3.32"],
                "msg20": ["192.168.3.32"]}
        return body
    else:
        pass


# mailbox_and_xyk
@app.post("/api/mailbox_and_xyk")
async def mailbox_and_xyk(data: Passport):
    if data.mailbox_and_xyk is not None:
        body = {"msg1": ["13613415737@163.com"],
                "msg2": ["13613415737@163.com"],
                "msg3": ["13613415737@163.com"],
                "msg4": ["13613415737@163.com"],
                "msg5": ["13613415737@163.com"],
                "msg6": ["13613415737@163.com"],
                "msg7": ["13613415737@163.com"],
                "msg8": ["13613415737@163.com"],
                "msg9": ["13613415737@163.com"],
                "msg10": ["13613415737@163.com"],
                "msg11": ["6227534800718027"],
                "msg12": ["6227534800718027"],
                "msg13": ["6227534800718027"],
                "msg14": ["6227534800718027"],
                "msg15": ["6227534800718027"],
                "msg16": ["6227534800718027"],
                "msg17": ["6227534800718027"],
                "msg18": ["6227534800718027"],
                "msg19": ["6227534800718027"],
                "msg20": ["6227534800718027"]}
        return body
    else:
        pass


# mailbox_and_idcard
@app.post("/api/mailbox_and_idcard")
async def mailbox_and_idcard(data: Passport):
    if data.mailbox_and_idcard is not None:
        body = {"msg1": ["13613415737@163.com"],
                "msg2": ["13613415737@163.com"],
                "msg3": ["13613415737@163.com"],
                "msg4": ["13613415737@163.com"],
                "msg5": ["13613415737@163.com"],
                "msg6": ["13613415737@163.com"],
                "msg7": ["13613415737@163.com"],
                "msg8": ["13613415737@163.com"],
                "msg9": ["13613415737@163.com"],
                "msg10": ["13613415737@163.com"],
                "msg11": ["142303199905033631"],
                "msg12": ["142303199905033631"],
                "msg13": ["142303199905033631"],
                "msg14": ["142303199905033631"],
                "msg15": ["142303199905033631"],
                "msg16": ["142303199905033631"],
                "msg17": ["142303199905033631"],
                "msg18": ["142303199905033631"],
                "msg19": ["142303199905033631"],
                "msg20": ["142303199905033631"]}
        return body
    else:
        pass


# iphone_and_creditcode
@app.post("/api/iphone_and_creditcode")
async def iphone_and_creditcod(data: Passport):
    if data.iphone_and_creditcod is not None:
        body = {"msg1": ["13613415737"],
                "msg2": ["13613415737"],
                "msg3": ["13613415737"],
                "msg4": ["13613415737"],
                "msg5": ["13613415737"],
                "msg6": ["13613415737"],
                "msg7": ["13613415737"],
                "msg8": ["13613415737"],
                "msg9": ["13613415737"],
                "msg10": ["13613415737"],
                "msg11": ["91310109MA1G5KN01M"],
                "msg12": ["91310109MA1G5KN01M"],
                "msg13": ["91310109MA1G5KN01M"],
                "msg14": ["91310109MA1G5KN01M"],
                "msg15": ["91310109MA1G5KN01M"],
                "msg16": ["91310109MA1G5KN01M"],
                "msg17": ["91310109MA1G5KN01M"],
                "msg18": ["91310109MA1G5KN01M"],
                "msg19": ["91310109MA1G5KN01M"],
                "msg20": ["91310109MA1G5KN01M"]
                }
        return body
    else:
        pass


# iphone_and_ipaddr
@app.post("/api/iphone_and_ipaddr")
async def iphone_and_ipaddr(data: Passport):
    if data.iphone_and_ipaddr is not None:
        body = {"msg1": ["13613415737"],
                "msg2": ["13613415737"],
                "msg3": ["13613415737"],
                "msg4": ["13613415737"],
                "msg5": ["13613415737"],
                "msg6": ["13613415737"],
                "msg7": ["13613415737"],
                "msg8": ["13613415737"],
                "msg9": ["13613415737"],
                "msg10": ["13613415737"],
                "msg11": ["192.168.3.32"],
                "msg12": ["192.168.3.32"],
                "msg13": ["192.168.3.32"],
                "msg14": ["192.168.3.32"],
                "msg15": ["192.168.3.32"],
                "msg16": ["192.168.3.32"],
                "msg17": ["192.168.3.32"],
                "msg18": ["192.168.3.32"],
                "msg19": ["192.168.3.32"],
                "msg20": ["192.168.3.32"]
                }
        return body
    else:
        pass


# iphone_and_xyk
@app.post("/api/iphone_and_xyk")
async def iphone_and_xyk(data: Passport, ):
    if data.iphone_and_xyk is not None:
        body = {"msg1": ["13613415737"],
                "msg2": ["13613415737"],
                "msg3": ["13613415737"],
                "msg4": ["13613415737"],
                "msg5": ["13613415737"],
                "msg6": ["13613415737"],
                "msg7": ["13613415737"],
                "msg8": ["13613415737"],
                "msg9": ["13613415737"],
                "msg10": ["13613415737"],
                "msg11": ["6227534800718027"],
                "msg12": ["6227534800718027"],
                "msg13": ["6227534800718027"],
                "msg14": ["6227534800718027"],
                "msg15": ["6227534800718027"],
                "msg16": ["6227534800718027"],
                "msg17": ["6227534800718027"],
                "msg18": ["6227534800718027"],
                "msg19": ["6227534800718027"],
                "msg20": ["6227534800718027"]
                }
        return body
    else:
        pass


# iphone_and_idcard
@app.post("/api/iphone_and_idcard")
async def iphone_and_idcard(data: Passport):
    if data.iphone_and_idcard is not None:
        body = {"msg1": ["13613415737"],
                "msg2": ["13613415737"],
                "msg3": ["13613415737"],
                "msg4": ["13613415737"],
                "msg5": ["13613415737"],
                "msg6": ["13613415737"],
                "msg7": ["13613415737"],
                "msg8": ["13613415737"],
                "msg9": ["13613415737"],
                "msg10": ["13613415737"],
                "msg11": ["142303199905033631"],
                "msg12": ["142303199905033631"],
                "msg13": ["142303199905033631"],
                "msg14": ["142303199905033631"],
                "msg15": ["142303199905033631"],
                "msg16": ["142303199905033631"],
                "msg17": ["142303199905033631"],
                "msg18": ["142303199905033631"],
                "msg19": ["142303199905033631"],
                "msg20": ["142303199905033631"]
                }
        return body
    else:
        pass


# creditcode_and_ipaddr
@app.post("/api/creditcode_and_ipaddr")
async def creditcode_and_ipaddr(data: Passport):
    if data.creditcode_and_ipaddr is not None:
        body = {"msg1": ["91310109MA1G5KN01M"],
                "msg2": ["91310109MA1G5KN01M"],
                "msg3": ["91310109MA1G5KN01M"],
                "msg4": ["91310109MA1G5KN01M"],
                "msg5": ["91310109MA1G5KN01M"],
                "msg6": ["91310109MA1G5KN01M"],
                "msg7": ["91310109MA1G5KN01M"],
                "msg8": ["91310109MA1G5KN01M"],
                "msg9": ["91310109MA1G5KN01M"],
                "msg10": ["91310109MA1G5KN01M"],
                "msg11": ["192.168.3.32"],
                "msg12": ["192.168.3.32"],
                "msg13": ["192.168.3.32"],
                "msg14": ["192.168.3.32"],
                "msg15": ["192.168.3.32"],
                "msg16": ["192.168.3.32"],
                "msg17": ["192.168.3.32"],
                "msg18": ["192.168.3.32"],
                "msg19": ["192.168.3.32"],
                "msg20": ["192.168.3.32"]
                }
        return body
    else:
        pass


# creditcode_and_xyk
@app.post("/api/creditcode_and_xyk")
async def creditcode_and_xyk(data: Passport):
    if data.creditcode_and_xyk is not None:
        body = {"msg1": ["91310109MA1G5KN01M"],
                "msg2": ["91310109MA1G5KN01M"],
                "msg3": ["91310109MA1G5KN01M"],
                "msg4": ["91310109MA1G5KN01M"],
                "msg5": ["91310109MA1G5KN01M"],
                "msg6": ["91310109MA1G5KN01M"],
                "msg7": ["91310109MA1G5KN01M"],
                "msg8": ["91310109MA1G5KN01M"],
                "msg9": ["91310109MA1G5KN01M"],
                "msg10": ["91310109MA1G5KN01M"],
                "msg11": ["6227534800718027"],
                "msg12": ["6227534800718027"],
                "msg13": ["6227534800718027"],
                "msg14": ["6227534800718027"],
                "msg15": ["6227534800718027"],
                "msg16": ["6227534800718027"],
                "msg17": ["6227534800718027"],
                "msg18": ["6227534800718027"],
                "msg19": ["6227534800718027"],
                "msg20": ["6227534800718027"]
                }
        return body
    else:
        pass


# creditcode_and_idcard
@app.post("/api/creditcode_and_idcard")
async def creditcode_and_idcard(data: Passport):
    if data.creditcode_and_idcard is not None:
        body = {"msg1": ["91310109MA1G5KN01M"],
                "msg2": ["91310109MA1G5KN01M"],
                "msg3": ["91310109MA1G5KN01M"],
                "msg4": ["91310109MA1G5KN01M"],
                "msg5": ["91310109MA1G5KN01M"],
                "msg6": ["91310109MA1G5KN01M"],
                "msg7": ["91310109MA1G5KN01M"],
                "msg8": ["91310109MA1G5KN01M"],
                "msg9": ["91310109MA1G5KN01M"],
                "msg10": ["91310109MA1G5KN01M"],
                "msg11": ["142303199905033631"],
                "msg12": ["142303199905033631"],
                "msg13": ["142303199905033631"],
                "msg14": ["142303199905033631"],
                "msg15": ["142303199905033631"],
                "msg16": ["142303199905033631"],
                "msg17": ["142303199905033631"],
                "msg18": ["142303199905033631"],
                "msg19": ["142303199905033631"],
                "msg20": ["142303199905033631"]
                }
        return body
    else:
        pass


# xyk_and_ipaddr
@app.post("/api/xyk_and_ipaddr")
async def xyk_and_ipaddr(data: Passport):
    if data.xyk_and_ipaddr is not None:
        body = {"msg1": ["6227534800718027"],
                "msg2": ["6227534800718027"],
                "msg3": ["6227534800718027"],
                "msg4": ["6227534800718027"],
                "msg5": ["6227534800718027"],
                "msg6": ["6227534800718027"],
                "msg7": ["6227534800718027"],
                "msg8": ["6227534800718027"],
                "msg9": ["6227534800718027"],
                "msg10": ["6227534800718027"],
                "msg11": ["192.168.3.32"],
                "msg12": ["192.168.3.32"],
                "msg13": ["192.168.3.32"],
                "msg14": ["192.168.3.32"],
                "msg15": ["192.168.3.32"],
                "msg16": ["192.168.3.32"],
                "msg17": ["192.168.3.32"],
                "msg18": ["192.168.3.32"],
                "msg19": ["192.168.3.32"],
                "msg20": ["192.168.3.32"]
                }
        return body
    else:
        pass


# idcard_and_ipaddr
@app.post("/api/idcard_and_ipaddr")
async def idcard_and_ipaddr(data: Passport):
    if data.idcard_and_ipaddr is not None:
        body = {"msg1": ["142303199905033631"],
                "msg2": ["142303199905033631"],
                "msg3": ["142303199905033631"],
                "msg4": ["142303199905033631"],
                "msg5": ["142303199905033631"],
                "msg6": ["142303199905033631"],
                "msg7": ["142303199905033631"],
                "msg8": ["142303199905033631"],
                "msg9": ["142303199905033631"],
                "msg10": ["142303199905033631"],
                "msg11": ["192.168.3.32"],
                "msg12": ["192.168.3.32"],
                "msg13": ["192.168.3.32"],
                "msg14": ["192.168.3.32"],
                "msg15": ["192.168.3.32"],
                "msg16": ["192.168.3.32"],
                "msg17": ["192.168.3.32"],
                "msg18": ["192.168.3.32"],
                "msg19": ["192.168.3.32"],
                "msg20": ["192.168.3.32"]
                }
        return body
    else:
        pass


# idcard_and_xyk
@app.post("/api/idcard_and_xyk")
async def idcard_and_xyk(data: Passport):
    if data.idcard_and_xyk is not None:
        body = {"msg1": ["142303199905033631"],
                "msg2": ["142303199905033631"],
                "msg3": ["142303199905033631"],
                "msg4": ["142303199905033631"],
                "msg5": ["142303199905033631"],
                "msg6": ["142303199905033631"],
                "msg7": ["142303199905033631"],
                "msg8": ["142303199905033631"],
                "msg9": ["142303199905033631"],
                "msg10": ["142303199905033631"],
                "msg11": ["6227534800718027"],
                "msg12": ["6227534800718027"],
                "msg13": ["6227534800718027"],
                "msg14": ["6227534800718027"],
                "msg15": ["6227534800718027"],
                "msg16": ["6227534800718027"],
                "msg17": ["6227534800718027"],
                "msg18": ["6227534800718027"],
                "msg19": ["6227534800718027"],
                "msg20": ["6227534800718027"]
                }
        return body
    else:
        pass


@app.post("/api/HKandMacau")
async def HKandMacau(data: Passport):
    if data.HKandMacau is not None:
        body = {"msg1": ["C20230227"],
                "msg2": ["C20230227"],
                "msg3": ["C20230227"],
                "msg4": ["C20230227"],
                "msg5": ["C20230227"],
                "msg6": ["C20230227"],
                "msg7": ["C20230227"],
                "msg8": ["C20230227"],
                "msg9": ["C20230227"],
                "msg10": ["C20230227"]}

        return body
    else:
        pass


@app.post("/api/car")
async def car(data: Passport):
    if data.car is not None:
        body = {"msg1": ["湘A88888"],
                "msg2": ["湘A88888"],
                "msg3": ["湘A88888"],
                "msg4": ["湘A88888"],
                "msg5": ["湘A88888"],
                "msg6": ["湘A88888"],
                "msg7": ["湘A88888"],
                "msg8": ["湘A88888"],
                "msg9": ["湘A88888"],
                "msg10": ["湘A88888"]}

        return body

    else:
        pass


@app.post("/api/mlxy")
async def mlxy(data: Passport):
    if data.mlxy is not None:
        body = {"msg1": ["19971228271471"],
                "msg2": ["19971228271471"],
                "msg3": ["19971228271471"],
                "msg4": ["19971228271471"],
                "msg5": ["19971228271471"],
                "msg6": ["19971228271471"],
                "msg7": ["19971228271471"],
                "msg8": ["19971228271471"],
                "msg9": ["19971228271471"],
                "msg10": ["19971228271471"]}
        return body
    else:
        pass


@app.post("/api/xyk")
async def xyk(data: Passport):
    if data.xyk is not None:
        body = {"msg1": ["6227534800718027"],
                "msg2": ["6227534800718027"],
                "msg3": ["6227534800718027"],
                "msg4": ["6227534800718027"],
                "msg5": ["6227534800718027"],
                "msg6": ["6227534800718027"],
                "msg7": ["6227534800718027"],
                "msg8": ["6227534800718027"],
                "msg9": ["6227534800718027"],
                "msg10": ["6227534800718027"]}
        return body
    else:
        pass


@app.post("/api/ssn")
async def ssn(data: Passport):
    if data.ssn is not None:
        body = {"msg1": ["818-89-9988"],
                "msg2": ["818-89-9988"],
                "msg3": ["818-89-9988"],
                "msg4": ["818-89-9988"],
                "msg5": ["818-89-9988"],
                "msg6": ["818-89-9988"],
                "msg7": ["818-89-9988"],
                "msg8": ["818-89-9988"],
                "msg9": ["818-89-9988"],
                "msg10": ["818-89-9988"]}
        return body
    else:
        pass


@app.post("/api/address")
async def address(data: Passport):
    if data.address is not None:
        body = {"msg1": ["北京市朝阳区东三环南银大厦915"],
                "msg2": ["北京市朝阳区东三环南银大厦915"],
                "msg3": ["北京市朝阳区东三环南银大厦915"],
                "msg4": ["北京市朝阳区东三环南银大厦915"],
                "msg5": ["北京市朝阳区东三环南银大厦915"],
                "msg6": ["北京市朝阳区东三环南银大厦915"],
                "msg7": ["北京市朝阳区东三环南银大厦915"],
                "msg8": ["北京市朝阳区东三环南银大厦915"],
                "msg9": ["北京市朝阳区东三环南银大厦915"],
                "msg10": ["北京市朝阳区东三环南银大厦915"]}
        return body
    else:
        pass


@app.post("/api/yyzz")
async def yyzz(data: Passport):
    if data.yyzz is not None:
        body = {"msg1": ["91310107133711201R"],
                "msg2": ["91310107133711201R"],
                "msg3": ["91310107133711201R"],
                "msg4": ["91310107133711201R"],
                "msg5": ["91310107133711201R"],
                "msg6": ["91310107133711201R"],
                "msg7": ["91310107133711201R"],
                "msg8": ["91310107133711201R"],
                "msg9": ["91310107133711201R"],
                "msg10": ["91310107133711201R"]}
        return body
    else:
        pass


@app.post("/api/v6")
async def v6(data: Passport):
    if data.v6 is not None:
        body = {"msg1": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg2": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg3": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg4": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg5": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg6": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg7": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg8": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg9": ["2409:8c20:1833:2000:0:1:afd:2a75"],
                "msg10": ["2409:8c20:1833:2000:0:1:afd:2a75"]}
        return body
    else:
        pass


@app.post("/api/car_num")
async def car_num(data: Passport):
    if data.car_num is not None:
        body = {"msg1": ["LSVAA418192763253"],
                "msg2": ["LSVAA418192763253"],
                "msg3": ["LSVAA418192763253"],
                "msg4": ["LSVAA418192763253"],
                "msg5": ["LSVAA418192763253"],
                "msg6": ["LSVAA418192763253"],
                "msg7": ["LSVAA418192763253"],
                "msg8": ["LSVAA418192763253"],
                "msg9": ["LSVAA418192763253"],
                "msg10": ["LSVAA418192763253"]}
        return body
    else:
        pass


@app.post("/api/mac")
async def mac(data: Passport):
    if data.mac is not None:
        body = {"msg1": ["F4-7B-09-D5-C2-26"],
                "msg2": ["F4-7B-09-D5-C2-26"],
                "msg3": ["F4-7B-09-D5-C2-26"],
                "msg4": ["F4-7B-09-D5-C2-26"],
                "msg5": ["F4-7B-09-D5-C2-26"],
                "msg6": ["F4-7B-09-D5-C2-26"],
                "msg7": ["F4-7B-09-D5-C2-26"],
                "msg8": ["F4-7B-09-D5-C2-26"],
                "msg9": ["F4-7B-09-D5-C2-26"],
                "msg10": ["F4-7B-09-D5-C2-26"]}
        return body
    else:
        pass


@app.post("/api/zjxy")
async def zjxy(data: Passport):
    if data.zjxy is not None:
        body = {"msg1": ["耶和华见证会"],
                "msg2": ["耶和华见证会"],
                "msg3": ["耶和华见证会"],
                "msg4": ["耶和华见证会"],
                "msg5": ["耶和华见证会"],
                "msg6": ["耶和华见证会"],
                "msg7": ["耶和华见证会"],
                "msg8": ["耶和华见证会"],
                "msg9": ["耶和华见证会"],
                "msg10": ["耶和华见证会"]}
        return body
    else:
        pass


@app.post("/api/IMEI")
async def IMEI(data: Passport):
    if data.IMEI is not None:
        body = {"msg1": ["011472001975695"],
                "msg2": ["011472001975695"],
                "msg3": ["011472001975695"],
                "msg4": ["011472001975695"],
                "msg5": ["011472001975695"],
                "msg6": ["011472001975695"],
                "msg7": ["011472001975695"],
                "msg8": ["011472001975695"],
                "msg9": ["011472001975695"],
                "msg10": ["011472001975695"]}
        return body
    else:
        pass


@app.post("/api/linux_password")
async def linux_password(data: Passport):
    if data.linux_password is not None:
        body = {"msg1": ["root:x:0:0:root:/root:/bin/bash"],
                "msg2": ["daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin"],
                "msg3": ["sys:x:3:3:sys:/dev:/usr/sbin/nologin"],
                "msg4": ["sync:x:4:65534:sync:/bin:/bin/sync"],
                "msg5": ["games:x:5:60:games:/usr/games:/usr/sbin/nologin"],
                "msg6": ["man:x:6:12:man:/var/cache/man:/usr/sbin/nologin"],
                "msg7": ["lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin"],
                "msg8": ["mail:x:8:8:mail:/var/mail:/usr/sbin/nologin"],
                "msg9": ["news:x:9:9:news:/var/spool/news:/usr/sbin/nologin"],
                "msg10": ["uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin"]}
        return body
    else:
        pass


@app.post("/api/linux_shadow")
async def linux_shadow(data: Passport):
    if data.linux_shadow is not None:
        body = {"msg1": ["daemon:*:18484:0:99999:7:::"],
                "msg2": ["bin:*:18484:0:99999:7:::"],
                "msg3": ["sys:*:18484:0:99999:7:::"],
                "msg4": ["sync:*:18484:0:99999:7:::"],
                "msg5": ["games:*:18484:0:99999:7:::"],
                "msg6": ["man:*:18484:0:99999:7:::"],
                "msg7": ["lp:*:18484:0:99999:7:::"],
                "msg8": ["mail:*:18484:0:99999:7:::"],
                "msg9": ["news:*:18484:0:99999:7:::"],
                "msg10": ["uucp:*:18484:0:99999:7:::"]
                }
        return body
    else:
        pass


@app.post("/api/pem")
async def pem(data: Passport):
    if data.pem is not None:
        body = {"msg1": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg2": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg3": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg4": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg5": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg6": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg7": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg8": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg9": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----'''],
                "msg10": ['''-----BEGIN CERTIFICATE-----
oodWqxtyvMyc716uT9ATdYxYA9XvBSXYAdE5QK7+TMId56AkChq/GCUCAwEAATAN
BgkqhkiG9w0BAQsFAAOCAQEAgP1AYLoVTlcBK2qQU2o7oxz3V/OSyR2e3dn11h2X
HzF3j/RAnU/RlHPy0I8dtyPj7eGi5UhmB1YC+NObLmcFHPqg8zBwDtk+rlfPsO4K
8iJ01eAYOzxx5gRuiFwHfpZFjjSHM2ovLTYHYRWT/xFzJK5bWtFd0TO3LnQk8/bc
8JHl5QmLZazsOgTl016Zm1FjhvbrDW0KhYnZzzwy/WcvSRalSZqWwgmXpKQk3jud
s+eWNmwrMNdY3TdmQzo3ONCy2oWH4KUYfJcRY/0RPq4F5k0FEJFWn9Aksf46lcFn
F6YP7Yd/h2jlx6f+0alRXPWndVRkRe6Yhlh6BX/MeSAhJQ==
-----END CERTIFICATE-----''']
                }
        return body
    else:
        pass


@app.get("/download", summary="下载文件")
async def download_file():
    body = {"msg": "download"}
    return body


@app.post("/notoken")
async def notoken(notoken: str):
    body = {"msg": notoken}
    return body



@app.post("/11")
async def gpfw(data: Data_qaq):
    if data.gpfw == "1":
        body = {"msg": "测试高频访问"}
        return body
    else:
        body1 = {"msg": f"no data"}
        return body1


@app.get("/api")
async def bianlijiekou(a: int, b: int):
    body = {"msg1": f"{a}",
            "msg2": f"{b}"}
    return body


@app.get("/search")
async def search(a: int):
    body = {"msg1": f"{a}"}
    return body


@app.get("/12")
async def bianlijiekou(a: int, b: int):
    body = {
        "msg2": f"{b}",
        "msg3": f"{b}",
        "msg4": f"{b}",
        "msg5": f"{b}",
        "msg6": f"{b}",
        "msg7": f"{b}"}
    return body


@app.get("/search")
async def search(a: int):
    body = {"msg1": f"{a}"}
    return body


class UsernameAndPassWord(BaseModel):
    username: str = None
    password: str = None
    new_password: str = None
    status: str = None


@app.post("/register")
def register(data: UsernameAndPassWord):
    if data.username is not None and data.password == data.new_password:
        # 以写入模式打开文件，将功能赋予变量f
        with open("msg.txt", 'a+', encoding='utf-8') as f:
            f.write(f"username:{data.username},password:{data.password}")
            body = {"code": 200, "msg": "register_success"}
            return body
    else:
        pass


@app.post("/login")
def login(data1: UsernameAndPassWord):
    f = open("msg.txt")
    data = f.read()
    print(data)
    if data1.username in data and data1.password in data:
        body = {"code": 200, "msg": "login_success"}
        return body
    else:
        pass


# 登录后退出
@app.post("/logout")
def quit_login(quit_data: UsernameAndPassWord):
    if quit_data.status == "logout":
        body = {"code": 200, "msg": "logout_success"}
        return body
    else:
        pass


class PhoneAndRegister(BaseModel):
    phone: str = None
    Verification_code: str = None


@app.post("/phone_register")
def register(data: PhoneAndRegister):
    if data.phone is not None:
        # 将注册的手机号添加到文件中，存储手机号信息。
        with open("phone_msg.txt", 'a+', encoding='utf-8') as f:
            f.write(f"phone:{data.phone}")
        # 生成验证码
        data.Verification_code = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            data.Verification_code += ch
            print(data.Verification_code)
        # 将验证码传入文件（覆盖写入）
        if len(data.Verification_code) == 6:
            with open("Verification_code.txt", 'w+', encoding='utf-8') as f:
                f.write(f"{data.Verification_code}")
                body = {"code": 200, "msg": "Phone_register_success", "verification_code": data.Verification_code,
                        'phone': data.phone}
                return body
    else:
        pass


@app.post("/phone_login")
def login(dataa: PhoneAndRegister):
    # 读取手机号
    f = open("phone_msg.txt")
    data1 = f.read()
    print(data1)
    # 读取验证码
    f = open("Verification_code.txt")
    data2 = f.read()
    print(data1)
    if dataa.phone in data1 and data2 == dataa.Verification_code:
        body = {"code": 200, "msg": "phone_login_success"}
        return body
    else:
        pass


class MailboxAndRegister(BaseModel):
    mailbox: str = None
    Verification_mailbox_code: str = None
    mailbox_id: str = None
    update_mailbox: str = None
    mailbox_msg: str = None
    search: str = None


@app.post("/mailbox_register")
def register(data: MailboxAndRegister):
    if data.mailbox is not None:
        # 将注册的邮箱添加到文件中。
        # 文件名
        file_name = "mailbox_msg.txt"
        # 添加的数据
        jsonobject = {
            "mailbox": data.mailbox,
            "mailbox_id": "1"
        }
        # 以附加写入的方式打开文件，
        file = open(file_name, "a+")
        json.dump(jsonobject, file)
        file.close()

        # 生成验证码
        data.Verification_mailbox_code = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            data.Verification_mailbox_code += ch
            print(data.Verification_mailbox_code)
            if len(data.Verification_mailbox_code) == 6:
                # 将验证码传入文件（覆盖写入）
                with open("Verification_mailbox_code.txt", 'a+', encoding='utf-8') as f:
                    f.write(f"{data.Verification_mailbox_code}")
                    body = {"code": 200, "msg": "mailbox_register_success",
                            "verification_mailbox_code": data.Verification_mailbox_code}
                    return body
    else:
        pass


@app.post("/mailbox_login")
def login(dataa: MailboxAndRegister):
    # 读取邮箱
    f = open("mailbox_msg.txt")
    data1 = f.read()
    print(data1)
    # 读取验证码
    f = open("Verification_mailbox_code.txt")
    data2 = f.read()
    print(data2)
    # 校验输入的邮箱和验证码是否正确
    if dataa.mailbox is not None:
        body = {"code": 200, "msg": "mailbox_login_success",
                "mailbox_info": {"mailbox": dataa.mailbox, "mailbox_id": data1}}
        return body
    else:
        pass


# 数据查询
@app.post("/query")
def query_mailbox(query_data: MailboxAndRegister):
    if query_data.search is not None:
        body = {
            "code": 200,
            "msg": "search_success"
        }

        return body
    else:
        pass


# 数据导出
@app.post("/download")
def export_mailbox(export_data: MailboxAndRegister):
    f = open("mailbox_msg.txt", "r")
    data = f.read()
    print(data)
    type(data)
    if export_data.mailbox_id == "1":
        df = DataFrame({"mailbox_id": [2, 22, 23], "mailbox": ['KEN', 'John', 'JIMI']})
        df.to_csv('test.csv')
        body = {"code": 200, "msg": "download_mailbox_success",
                }
        return body
    else:
        pass


# 数据增加
@app.post("/create")
def create_mailbox(create_data: MailboxAndRegister):
    f = open("mailbox_msg.txt")
    data = f.read()
    print(data)
    type(data)
    # 判断添加的数据是否已经存在
    if create_data.mailbox not in data:
        with open("mailbox_msg.txt", "a+", encoding='utf-8') as f:
            f.write(create_data.mailbox)
            body = {"code": 200, "msg": "create_mailbox_success",
                    "mailbox_info": create_data.mailbox}
            return body
    else:
        pass


# 数据删除
@app.post("/delete")
def delete_mailbox(delete_data: MailboxAndRegister):
    f = open("mailbox_msg.txt")
    data = f.read()
    print(data)
    type(data)
    # 判断添加的数据是否已经存在
    if delete_data.mailbox in data:
        with open("mailbox_msg.txt", "a+", encoding='utf-8') as f:
            f.truncate(0)
            body = {"code": 200, "msg": "delete_mailbox_success"
                    }
            return body
    else:
        pass


# 数据更新
@app.post("/update")
def update_mailbox(update_data: MailboxAndRegister):
    f = open("mailbox_msg.txt")
    data = f.read()
    print(data)
    type(data)
    # 判断添加的数据是否已经存在
    if update_data.mailbox in data:
        with open("mailbox_msg.txt", "a+", encoding='utf-8') as f:
            f.truncate(0)
            f.write(update_data.update_mailbox)
            data1 = f.read()
            body = {"code": 200, "msg": "update_mailbox_success",
                    "mailbox_info": data1
                    }
            return body
    else:
        pass


# 发送邮箱
@app.post("/send_mailbox")
def send_mailbox(send_data: MailboxAndRegister):
    f1 = open("user_mailbox.txt", "w+")
    f = open("mailbox_msg.txt")
    data = f.read()
    if send_data.mailbox == data:
        f1.write(send_data.mailbox_msg)
        body = {"code": 200, "msg": "send_mailbox_success"
                }
        return body


# 异部地区访问
@app.post("/xff")
def xff(data: MailboxAndRegister, X_Forwarded_For: Union[str, None] = Header(default=None)):
    """ 异步地区访问 """
    return {"code": 200,
            "X-Forwarded-For": X_Forwarded_For

            }


# 异常的批量导出行为
@app.get("/export")
def export(content_disposition: Union[str, None] = Header(default=None)):
    """ 异常的批量导出行为 """
    return {"code": 200,
            "content_disposition": content_disposition,
            "content_disposition1": content_disposition,
            "content_disposition2": content_disposition,
            "content_disposition3": content_disposition,
            "content_disposition5": content_disposition,
            "content_disposition4": content_disposition,
            "content_disposition6": content_disposition,
            "msg": "export_succeed"

            }


# 测试有token字段，是否会被记录
@app.get("/token")
def export(token: Union[str, None] = Header(default=None)):
    """ 测试有token字段，是否会被记录"""
    return {"code": 200,
            "token": token,
            }


@app.post("/api/credit_card")
async def credit_card(data: Passport):
    if data.credit_card is not None:
        body = {"msg1": ["6225100024522822"],
                "msg2": ["6259063220999695"],
                "msg3": ["6259063220999695"],
                "msg4": ["6259063220999695"],
                "msg5": ["6259063220999695"],
                "msg6": ["6259063220999695"],
                "msg7": ["6229190000067784"],
                "msg8": ["6259063220999695"],
                "msg9": ["6259063220999695"],
                "msg10": ["6259063220999695"]
                }
        return body
    else:
        pass


@app.post("/10")
async def wsqfwhqmgxx2(data: Data_qaq):
    """ 多种敏感信息 """
    if data.xx == "1":
        body = {"敏感信息1": "15510222699",
                "敏感信息2": "430423196612050021",
                "敏感信息3": "192.168.3.204",
                "敏感信息4": "195124512@qq.com",
                "敏感信息5": "湘A88888",
                "敏感信息6": "6227534800718027",
                "敏感信息7": "G28333055",
                "敏感信息8": "root:x:0:0:root:/root:/bin/bash",
                "敏感信息9": "011472001975695",
                "敏感信息10": "耶和华见证会"}
        return body
    else:
        return {"msg": f"no data"}


@app.get("/info_9")
def info_9():
    """ 9条敏感数据"""
    body = {
        "msg1": ["E0-73-E7-31-25-FD"],
        "msg2": ["64-49-7D-77-E9-4F"],
        "msg3": ["66-49-7D-77-E9-4E"],
        "msg4": ["00-50-56-C0-00-01"],
        "msg5": ["00-50-56-C0-00-08"],
        "msg6": ["64-49-7D-77-E9-4E"],
        "msg7": ["64-49-7D-77-E9-52"],
        "msg8": ["64-49-7D-77-E9-52"],
        "msg9": ["64-49-7D-77-E9-52"],
    }
    return body


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
