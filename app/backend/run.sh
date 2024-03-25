#!/bin/bash

pip install requirements.txt
echo "Implemente aqui o script para executar a sua solução"

uvicorn main:app --port 3000 --reload
cd ..
npm run serve -- --port 8080
