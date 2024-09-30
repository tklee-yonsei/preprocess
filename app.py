from flask import Flask, jsonify, request

from coder.hamming_coder import HammingCoder
from coder.pass_through_coder import PassThroughCoder
from coder.repetition_coder import RepetitionCoder
from coder.xor_coder import XORCoder

app = Flask(__name__)

# 코딩 방법 매핑 - 인스턴스를 미리 생성하여 재사용
coders = {
    "pass": PassThroughCoder(),
    "hamming": HammingCoder(),
    "xor": XORCoder(),
    "repetition": RepetitionCoder(),
}


@app.route("/encode/<method>", methods=["POST"])
def encode(method):
    coder = coders.get(method)
    if coder is None or method not in coders:
        return jsonify({"error_code": 2001, "error": "Invalid encoding method"}), 400

    data_bits = request.json.get("data_bits")
    if data_bits is None:
        return jsonify({"error_code": 2002, "error": "Missing data_bits"}), 400

    try:
        coded_bits = coder.encode(data_bits)
    except ValueError as e:
        return jsonify({"error_code": 2003, "error": str(e)}), 400

    return jsonify({"coded_bits": coded_bits})


@app.route("/decode/<method>", methods=["POST"])
def decode(method):
    coder = coders.get(method)
    if coder is None:
        return jsonify({"error_code": 2001, "error": "Invalid decoding method"}), 400

    coded_bits = request.json.get("coded_bits")
    if coded_bits is None:
        return jsonify({"error_code": 2002, "error": "Missing coded_bits"}), 400

    try:
        decoded_bits = coder.decode(coded_bits)
    except ValueError as e:
        return jsonify({"error_code": 2003, "error": str(e)}), 400

    return jsonify({"decoded_bits": decoded_bits})


if __name__ == "__main__":
    app.run(port=5001)
