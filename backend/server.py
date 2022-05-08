from urllib import request
from flask import Flask, request
from flask_api import status
import pyautogui
import qrcode
import sys
import os
import io
import signal
import time
import socket
import tempfile
from PIL import Image
import PySimpleGUI as psg
from threading import Thread, Event

app = Flask(
    "numpad-backend",
    static_url_path="",
    static_folder="../frontend/build"
)

allowed_keys = [
    '/', '*', '-', '+', '.', 'enter', 'backspace',
    'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9'
]

@app.route('//')
def root():
    return app.send_static_file('index.html')

@app.route('/keypress', methods=['PUT'])
def keypress():
    key = request.args.get('key')
    # TODO
    # Get key
    # Get auth guid
    # Press key

    if not key in allowed_keys:
        return "", status.HTTP_200_OK

    pyautogui.keyDown(key)
    time.sleep(0.002)
    pyautogui.keyUp(key)
    return "", status.HTTP_200_OK

def get_server_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        return None
    finally:
        s.close()
    return ip

def show_pairing_gui(qr_img, qr_data, sentinel):

    temp_img = tempfile.NamedTemporaryFile(delete=False)
    b = io.BytesIO()
    qr_img.save(b, format='PNG')
    temp_img.write(b.getvalue())
    img_path = temp_img.name
    temp_img.close()

    layout = [
        [psg.Text("Scan code to connect")],
        [psg.Text("Close window to shut down server")],
        [psg.Image(img_path)],
        [psg.Text(f"Server URL: {qr_data}")],
    ]
    win = psg.Window(
        title="Offscreen Keyboard", 
        layout=layout
    )
    
    while not sentinel.is_set():
        event, values = win.read()
        if event ==  psg.WIN_CLOSED:
            break
    win.close()

    try:
        os.remove(img_path)
    except Exception:
        pass

    # TODO: This could be cleaner, but works
    sig = getattr(signal, "SIGKILL", signal.SIGTERM)
    os.kill(os.getpid(), sig)

if __name__ == '__main__':
    # Locally, use qr to point mobile to server
    # TODO: And pass over an auth token for the session!
    server_port = 8080
    qr_data = f"http://{get_server_ip()}:{server_port}"
    qr_img = qrcode.make(qr_data)

    sentinel = Event()
    gui_thread = Thread(target=show_pairing_gui, args=(qr_img, qr_data, sentinel))
    gui_thread.start()

    # TODO: https support, or something like that..Do our best to not internet-host the keyboard :)
    app.run(host='0.0.0.0', port=server_port)
    sentinel.set()
