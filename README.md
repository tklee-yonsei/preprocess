# Team 1 - Preprocessing API Documentation

This document provides an overview of the preprocessing APIs developed by Team 1. 
The preprocessing server handles signal normalization and filtering tasks. 
The APIs are available for both real and mock endpoints.

## API Endpoints

### 1. Normalize Signal

- **URL**: `/preprocess/normalize`
- **Method**: `POST`
- **Description**: Normalizes the given signal data.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "signal": [1, 2, 3, 4, 5]
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "normalized_signal": [0.2, 0.4, 0.6, 0.8, 1.0]
    }
    ```

### 2. Filter Signal

- **URL**: `/preprocess/filter`
- **Method**: `POST`
- **Description**: Applies a filter to the given signal data based on the specified filter type and cutoff frequency.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "signal": [1, 2, 3, 4, 5],
        "filter_type": "lowpass",
        "cutoff_frequency": 2.0
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "filtered_signal": [1, 2]
    }
    ```

## Mock API Endpoints

To facilitate development and testing, mock endpoints are provided to simulate the real API responses.

### 1. Mock Normalize Signal

- **URL**: `/mock/v1/preprocess/normalize`
- **Method**: `POST`
- **Description**: Simulates normalization of the given signal data.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "signal": [1, 2, 3, 4, 5]
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "normalized_signal": [0.2, 0.4, 0.6, 0.8, 1.0]
    }
    ```

### 2. Mock Filter Signal

- **URL**: `/mock/v1/preprocess/filter`
- **Method**: `POST`
- **Description**: Simulates filtering of the given signal data.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "signal": [1, 2, 3, 4, 5],
        "filter_type": "lowpass",
        "cutoff_frequency": 2.0
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**:
    ```json
    {
        "filtered_signal": [1, 2]
    }
    ```

## Getting Started

To run the preprocessing server, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.dev -t dev-python-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5001:5001 -v $(pwd):/app dev-python-server
    ```

The server will be available on `http://localhost:5001`.

## License

This project is licensed under the MIT License.