# RMQ to Core API Integration

This project demonstrates a simple integration between a RabbitMQ (RMQ) client and a Flask-based API server.

## Project Structure

The project consists of two main files:

1. `main.py`: This is the RMQ client script that fetches data from RMQ and sends it to the Core API.
2. `app.py`: This is the Flask-based API server that receives the data from the RMQ client and processes it.

## Usage

1. Ensure you have Python 3 installed on your system.
2. Install the required dependencies by running the following command:

pip install requests flask

3. ``` Start the Flask API server by running the following command in one terminal window: ```

python app.py

This will start the API server on `http://localhost:5005/api`.

4. In another terminal window, run the RMQ client script:

python main.py

This will send the data from the RMQ client to the Core API.

## How it Works

1. The `main.py` file contains two functions:
- `getDataFromRMQ()`: This function simulates fetching data from a RabbitMQ queue and returns a dictionary with the data.
- `sendDataToCore(payload)`: This function sends the data from the RMQ client to the Core API using the `requests` library.

2. The `app.py` file contains a Flask-based API server with a single route:
- `/api`: This route accepts POST requests and processes the data sent from the RMQ client. It simply prints the received payload and returns the same payload as the response.

When you run the `main.py` script, it calls the `getDataFromRMQ()` function to fetch the data and then passes it to the `sendDataToCore(payload)` function, which sends the data to the Core API. The API server in `app.py` receives the data, prints it, and returns the same data back to the client.

Feel free to modify the code to fit your specific use case and integration requirements.