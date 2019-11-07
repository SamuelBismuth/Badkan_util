from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route('/')
def index():
    return abort(404)


@app.route('/test/', methods=["POST"])
def test():
    response = request.get_json()
    print(response)
    return "Success"


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
