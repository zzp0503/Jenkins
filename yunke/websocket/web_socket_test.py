from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn, websocket

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:1025/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/api/web_socket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        head = websocket.headers
        await websocket.send_text(f"header:{head}")
        data = await websocket.receive()
        await websocket.send_text(f"Message text was: {data}")



# @app.websocket("/websocket/test01")
# def web_socket_test01(websocket: WebSocket):ss
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")


if __name__ == '__main__':
    uvicorn.run("web_socket_test:app", reload=True, host="0.0.0.0", port=1025)
