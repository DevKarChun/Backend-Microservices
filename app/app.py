from flask import Flask, jsonify, make_response, request


app = Flask(__name__)

@app.route('/api', methods = ['POST'])
def task():
    # time.sleep(1)
    payload = request.json
    print(payload)
    return make_response(
        jsonify(payload),
        200,
    )
    

if __name__ == '__main__':
    app.run(debug=False, host="localhost", port=5005)
    
    # API call hello world (recieve)