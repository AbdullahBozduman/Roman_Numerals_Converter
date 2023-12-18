#! /bin/bash
dnf update -y
dnf install python3
pip install flask
FOLDER="https://raw.githubusercontent.com/AbdullahBozduman/Project_101/master/static-web"
wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg
wget ${FOLDER}/cat3.png
cd /path/to/destination
python3 roman-numerals-converter-app.py