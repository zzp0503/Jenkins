from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_request():
    headers = dict(request.headers)
    args = dict(request.args)
    print("Request Headers:", headers)
    print("Request Args:", args)
    return jsonify({'headers': headers, 'args': args}), 200


@app.route('/api', methods=['POST'])
def post_request():
    headers = dict(request.headers)

    if request.content_type == 'application/x-www-form-urlencoded':
        data = dict(request.form)
        print("Request Headers:", headers)
        print("Request Form Data:", data)
        response_data = {'headers': headers, 'form_data': data}
        return jsonify(response_data), 200

    elif request.content_type == 'application/json':
        data = request.json
        print("Request Headers:", headers)
        print("Request JSON Data:", data)
        response_data = {'headers': headers, 'json_data': data}
        return jsonify(response_data), 200

    elif request.content_type == 'application/xml':
        data = request.data.decode('utf-8')
        print("Request Headers:", headers)
        print("Request XML Data:", data)
        response_data = {'headers': headers, 'xml_data': data}
        return jsonify(response_data), 200

    elif request.content_type == 'text/plain':
        data = request.data.decode('utf-8')
        print("Request Headers:", headers)
        print("Request Plain Text Data:", data)
        response_data = {'headers': headers, 'plain_text_data': data}
        return jsonify(response_data), 200

    return 'Unsupported Content-Type', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
