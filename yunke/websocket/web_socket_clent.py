import websocket, websockets


def websocket_req():
    while True:
        url = "ws://127.0.0.1:1025/api/web_socket"
        ws = websocket.create_connection(url=url)
        req_msg = input(f"请输入内容：")
        ws.send(req_msg)
        resp = ws.recv()
        if req_msg == "exit":
            exit_msg = input("是否确认退出，Y or N：")
            if exit_msg == "Y":
                print("选择Y,退出连接。")
                return False
            else:
                print("选择N,继续连接。")
        else:
            print(resp)


if __name__ == '__main__':
    websocket_req()
