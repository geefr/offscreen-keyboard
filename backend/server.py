##

from urllib import request
import uuid
from flask import Flask, request, make_response, render_template, abort, redirect, session
from flask_api import status
import keyboard
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

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

app = Flask(
    "offscreen-keyboard",
    static_url_path="",
    static_folder=resource_path("static")
)

allowed_keys = [
    '/', '*', '-', '+', '.', 'enter', 'backspace',
    'num 0', 'num 1', 'num 2', 'num 3', 'num 4', 'num 5', 'num 6',
    'num 7', 'num 8', 'num 9'
]


server_auth_data = str(uuid.uuid4().hex)

@app.route('//')
def root():
    auth_data = request.cookies.get('auth')
    if not auth_data:
        abort(404)
    if auth_data != server_auth_data:
        abort(404)
    return app.send_static_file('index.html')

@app.route('/keypress', methods=['PUT'])
def keypress():
    auth_data = request.cookies.get('auth')
    if not auth_data:
        abort(404)
    if auth_data != server_auth_data:
        abort(404)

    key = request.args.get('key')
    if not key in allowed_keys:
        abort(404)

    keyboard.press_and_release(key)
    return "", status.HTTP_200_OK

@app.route('/pair', methods=['GET'])
def pair():
    auth_data = request.args.get('auth')
    if not auth_data:
        abort(404)
    if auth_data != server_auth_data:
        abort(404)
    
    resp = make_response(redirect('/'))
    resp.set_cookie('auth', auth_data)
    return resp

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
        # [psg.Text("Close window to shut down server")],
        [psg.Image(img_path)],
        # [psg.Text(f"Server URL: {qr_data}")],
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
    server_port = 56165
    qr_data = f"http://{get_server_ip()}:{server_port}/pair?auth={server_auth_data}"
    qr_img = qrcode.make(qr_data)

    sentinel = Event()
    gui_thread = Thread(target=show_pairing_gui, args=(qr_img, qr_data, sentinel))
    gui_thread.start()

    # TODO: https support, or something like that..Do our best to not internet-host the keyboard :)
    app.run(host='0.0.0.0', port=server_port)
    sentinel.set()
