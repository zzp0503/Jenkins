import requests
from flask import Flask, request, redirect, url_for, render_template_string, send_from_directory
import os

app = Flask(__name__)

# HTML模板，包含GET和POST表单、超链接和重定向按钮
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>页面服务示例</title>
</head>
<body>
    <h1>POST表单提交</h1>
    <form method="post" action="/post">
        <input type="text" name="post_field" placeholder="输入POST数据" />
        <input type="submit" value="POST提交" />
    </form>

    <h1>子页面</h1>
    <a href="/get?query=example">点击这里携带参数跳转</a>

    <h1>GET请求提交</h1>
    <form method="get" action="/get_submit">
        <input type="text" name="get_field" placeholder="输入GET数据" />
        <input type="submit" value="GET提交" />
    </form>

    <h1>文件上传</h1>
    <form method="post" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" />
        <input type="submit" value="上传文件" />
    </form>

    <h1>文件下载</h1>
    <a href="/download?filename=test.txt">下载文件</a>

    <h1>重定向按钮</h1>
    <form method="get" action="/redirect?id=1">
        <input type="submit" value="重定向并携带参数" />
    </form>
    <a href="/refere?query=refere">超链接按钮</a>

    <script>
        // 示例JavaScript代码，通过AJAX发送JSON格式的POST请求
        function sendJsonPostRequest() {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/post_json', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function () {
                if (this.readyState === XMLHttpRequest.DONE) {
                    alert('JSON POST请求成功');
                }
            };
            xhr.send(JSON.stringify({ key: 'value' }));
        }
    </script>

    <button onclick="sendJsonPostRequest()">通过JS发送JSON POST</button>
</body>
</html>
'''

# 文件上传和下载的目录
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    # 返回HTML页面
    return render_template_string(HTML_TEMPLATE)


@app.route('/post', methods=['POST'])
def post():
    # 处理表单提交的POST请求
    post_data = request.form.get('post_field')
    # 打印请求头和请求参数
    print("请求头:", request.headers)
    print("POST请求参数:", post_data)
    print("请求URL:", request.url)
    return f"POST请求数据: {post_data}"


@app.route('/post_json', methods=['POST'])
def post_json():
    # 处理JSON格式的POST请求
    json_data = request.get_json()
    # 打印请求头和请求参数
    print("请求头:", request.headers)
    print("JSON请求参数:", json_data)
    print("请求URL:", request.url)
    return {'message': 'JSON POST请求成功', 'data': json_data}


@app.route('/get')
def get():
    # 处理GET请求
    query = request.args.get('query', default='无参数', type=str)
    # 打印请求头和请求参数
    print("请求头:", request.headers)
    print("GET请求参数:", query)
    print("请求URL:", request.url)
    return render_template_string(HTML_TEMPLATE)


@app.route('/get_submit', methods=['GET'])
def get_submit():
    # 处理GET请求提交
    get_data = request.args.get('get_field')
    # 打印请求头和请求参数
    print("请求头:", request.headers)
    print("GET提交参数:", get_data)
    print("请求URL:", request.url)
    return f"GET提交参数: {get_data}"


@app.route('/refere')
def refere():
    # 处理GET请求
    query = request.args.get('query', default='无参数', type=str)
    # 打印请求头和请求参数
    print("请求头:", request.headers)
    referer = request.headers.get('Referer')
    print("GET请求参数:", query)
    print("请求URL:", request.url)
    return f"GET请求参数: {query}，refere:{referer}"


@app.route('/redirect', methods=['GET'])
def redirect_to_get():
    # 处理重定向请求
    return redirect(url_for('get', query='redirected'))


@app.route('/upload', methods=['POST'])
def upload_file():
    # 处理文件上传
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # 打印请求头、请求参数和请求URL
        print("请求头:", request.headers)
        print("请求参数:", request.form)
        print("请求URL:", request.url)
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'File {filename} uploaded successfully'


@app.route('/download')
def download_file():
    # 处理文件下载
    filename = request.args.get('filename')
    if filename:
        # 打印请求头、请求参数和请求URL
        print("请求头:", request.headers)
        print("请求参数:", request.args)
        print("请求URL:", request.url)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    else:
        return 'No filename provided.'


if __name__ == '__main__':
    # 监听所有IP地址
    app.run(host='0.0.0.0', debug=True)