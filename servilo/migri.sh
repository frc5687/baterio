#!/usr/bin/env bash

if [ ! -d ".venv" ]; then
    python3 limak/db/migradoj.py
else
    . .venv/bin/activate; python limak/db/migradoj.py
fi
