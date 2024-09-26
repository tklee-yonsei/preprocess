from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/encode/<method>", methods=["POST"])
def encode(method):
    data_bits = request.json.get("data_bits")
    # Mock: 입력 데이터 그대로 반환
    coded_bits = data_bits
    return jsonify({"coded_bits": coded_bits})


@app.route("/decode/<method>", methods=["POST"])
def decode(method):
    coded_bits = request.json.get("coded_bits")
    # Mock: 입력 데이터 그대로 반환
    decoded_bits = coded_bits
    return jsonify({"decoded_bits": decoded_bits})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001)  # 모든 인터페이스에서 수신하도록 설정
