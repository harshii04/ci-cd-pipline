from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def landing_page():
    res = {
        "success": True,
        "message": 'CI/CD Demo'
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
