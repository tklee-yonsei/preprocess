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

## Getting Started

This section provides instructions on how to set up and run the preprocessing server in different environments.

### Local Development

To run the preprocessing server in a local development environment, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.dev -t dev-python-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5001:5001 -v $(pwd):/app --rm --name container__dev-python-server dev-python-server
    ```

The server will be available on `http://localhost:5001`.

### mock

To run the preprocessing server in a mock environment, ensure you have Docker installed and use the provided Dockerfile to build and run the server.

1. **Build the Docker image**:
    ```bash
    docker build -f Dockerfile.mock -t mock-server .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 6001:6001 --rm --name container__mock-server mock-server
    ```

The server will be available on `http://localhost:6001`.


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
