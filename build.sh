#!/usr/bin/env bash
pushd frontend
npm install
npm run build
popd

pushd backend
python -m venv venv

if [ "$(uname)" == "MINGw32_NT" ]; then
  source venv/Scripts/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
  source venv/Scripts/activate
else
  source venv/bin/activate
fi

pip install -r requirements.txt
pip install pyinstaller pyinstaller[encryption]

# --key encrypts the python bytecode in the executable
# This is actually simple to extract, so not all that secure
# But, it seems it's enough to raise our reputation with
# Microsoft Defender
pyinstaller --noconfirm -w -F --key=goawaymsdefender --version-file=../version.txt --add-data "../frontend/build;static" --onefile --hidden-import=flask_api.parsers --hidden-import=flask_api.renderers --name offscreen_keyboard server.py

popd
