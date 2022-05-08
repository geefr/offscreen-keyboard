# Offscreen Keyboard

A quick hack to run a numpad on my phone, as my laptop doesn't have one

Known Issues:
* Communication is unencrypted (HTTP)
  * But there's at least a session cookie
* I've only tested this on Windows so far

# Usage

* Download the latest release
* Run the executable
* Scan the QR code on a phone/tablet
* When finished, close the desktop window to shutdown the server

# Building

Requirements:
* Python
* npm
* The usual dev environment

Usage:
* `./run-dev.sh` to build and start server
* Navigate to server on your phone/other device
* Press buttons

![Screenshot](docs/numpad.png)
