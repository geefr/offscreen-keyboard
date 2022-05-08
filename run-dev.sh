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
python server.py

popd

