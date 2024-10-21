from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


# 处理 JSON 数据的路由
@app.route('/post-json', methods=['POST'])
def post_json():
    data = request.get_json()
    print(data)
    return jsonify(data)


# 处理表单数据的路由
@app.route('/post-form', methods=['POST'])
def post_form():
    # 使用 request.form 来获取表单数据
    form_data = request.form
    print(form_data)
    # 将表单数据转换为字典并返回
    return jsonify(dict(form_data))


@app.route('/get-data')
def get_data():
    # 获取 URL 中的查询参数
    query = request.args.get('query', default=None, type=str)
    if query is None:
        return jsonify({'error': 'No query parameter provided'}), 400
    print(f"Received GET request with query parameter: {query}")
    return jsonify({
        'query': query
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
