from urllib import request
from flask import Flask, request
from flask_api import status
import pyautogui
import time

app = Flask(
    "numpad-backend",
    static_url_path="",
    static_folder="../frontend/build"
)

@app.route('//')
def root():
    return app.send_static_file('index.html')

@app.route('/keypress', methods=['PUT'])
def keypress():
    key = request.args.get('key')
    print(f"Pressing key: {key}")
    # TODO
    # Get key
    # Get auth guid
    # Press key
    pyautogui.keyDown(key)
    time.sleep(0.002)
    pyautogui.keyUp(key)
    return "", status.HTTP_200_OK

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    # TODO
    # Generate auth guid
    # Make qrcode - server url and auth guid
    # Display desktop window for device pairing
