#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear --upload-unhashed-files
