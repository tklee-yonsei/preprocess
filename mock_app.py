from flask import Flask, jsonify, request

app = Flask(__name__)


# Mock endpoint for normalize
@app.route("/preprocess/normalize", methods=["POST"])
def mock_normalize():
    # 클라이언트로부터 받은 요청 데이터를 처리하여 출력 형식을 맞춥니다.
    input_data = request.json
    normalized_signal = input_data.get("signal", [])  # 입력의 "signal" 값을 그대로 사용
    response_data = {"normalized_signal": normalized_signal}
    return jsonify(response_data)


# Mock endpoint for filter
@app.route("/preprocess/filter", methods=["POST"])
def mock_filter():
    # 클라이언트로부터 받은 요청 데이터를 처리하여 출력 형식을 맞춥니다.
    input_data = request.json
    filtered_signal = input_data.get("signal", [])  # 입력의 "signal" 값을 그대로 사용
    response_data = {"filtered_signal": filtered_signal}
    return jsonify(response_data)


if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=6001)
