from flask import Flask, jsonify, request
from preprocess.preprocess_service import PreprocessorService

app = Flask(__name__)

# 서비스 클래스 인스턴스 생성
preprocessor_service = PreprocessorService()


@app.route("/preprocess/normalize", methods=["POST"])
def mock_normalize():
    input_data = request.json
    signal = input_data.get("signal", [])

    # 서비스 클래스의 normalize 메서드 호출
    normalized_signal = preprocessor_service.normalize(signal)

    response_data = {"normalized_signal": normalized_signal}
    return jsonify(response_data)


@app.route("/preprocess/filter", methods=["POST"])
def mock_filter():
    input_data = request.json
    signal = input_data.get("signal", [])
    filter_type = input_data.get("filter_type", "lowpass")
    cutoff_frequency = input_data.get("cutoff_frequency", 2.0)

    # 서비스 클래스의 filter 메서드 호출
    filtered_signal = preprocessor_service.filter(signal, filter_type, cutoff_frequency)

    response_data = {"filtered_signal": filtered_signal}
    return jsonify(response_data)


if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host="0.0.0.0", port=5001)
