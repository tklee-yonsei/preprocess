# 팀 1 - 채널 코딩 API 문서

채널 코딩을 위한 API 문서입니다/

## API 엔드포인트

### 1. 인코딩

- **URL**: `/encode/<method>`
- **Parameters**: 
  - `<method>`: `pass`, `hamming`, `repetition`
- **Method**: `POST`
- **Description**: 신호를 인코딩 후, 인코딩된 신호를 돌려줍니다.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "data_bits": "11010011"
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "coded_bits": "11010011"
    }
    ```

### 2. 디코딩

- **URL**: `/decode/<method>`
- **Parameters**: 
  - `<method>`: `pass`, `hamming`, `repetition`
- **Method**: `POST`
- **Description**: 신호를 인코딩 후, 인코딩된 신호를 돌려줍니다.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "coded_bits": "11010011"
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "decoded_bits": "11010011"
    }
    ```

## 에러

- **1001**: Invalid modulation/demodulation method
- **1002**: Missing bits data
- **1003**: Invalid bits format
- **1004**: Missing symbols data
- **1005**: Invalid symbols data format
- **1006**: Invalid action (WebSocket 전용)

## 시작하기

이 섹션에서는 다양한 환경에서 전처리 서버를 설정하고, 
실행하는 방법에 대한 지침을 제공합니다.

### 로컬 개발

로컬 개발 환경에서 전처리 서버를 실행하려면, 
Docker가 설치되어 있는지 확인하고, 
제공된 Dockerfile을 사용하여 서버를 빌드하고 실행하세요.

1. **Docker 이미지 빌드**:
    ```bash
    docker build -f Dockerfile.dev -t dev-python-server .
    ```

2. **Docker 컨테이너 실행**:
    ```bash
    docker run -p 5001:5001 -v $(pwd):/app --rm --name container__dev-python-server dev-python-server
    ```

서버는 `http://localhost:5001`에서 사용할 수 있습니다.

### mock

mock 환경에서 전처리 서버를 실행하려면, 
Docker가 설치되어 있는지 확인하고, 
제공된 Dockerfile을 사용하여 서버를 빌드하고 실행하세요.

1. **Docker 이미지 빌드**:
    ```bash
    docker build -f Dockerfile.mock -t mock-server .
    ```

2. **Docker 컨테이너 실행**:
    ```bash
    docker run -p 6002:6002 --rm --name container__mock-server mock-server
    ```

서버는 `http://localhost:6002`에서 사용할 수 있습니다.


### k8s

To deploy the preprocessing server on a Kubernetes cluster, follow these steps:

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.k8s -t preprocess-server .
    ```

2. **Push the Docker image to a registry** (if not already available):
    ```bash
    docker tag preprocess-server:latest your-registry/preprocess-server:latest
    docker push your-registry/preprocess-server:latest
    ```

3. **Apply the Kubernetes deployment and service configurations**:
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

The server will be available on the cluster IP specified by the Kubernetes service.

## License

This project is licensed under the MIT License.
