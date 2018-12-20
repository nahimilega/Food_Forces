#! /bin/bash

#Assuption python3 and google-chrome are installed in the PC

cd foodforces/
python3 manage.py runserver
google-chrome 127.0.0.1:8000/mainpage
