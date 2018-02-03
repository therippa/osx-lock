#!/bin/bash
source /Users/jbaker/.env/osx-lock/bin/activate
export FLASK_APP=/Users/jbaker/projects/osx-lock/main.py 
flask run --port=5685 --host=0.0.0.0

