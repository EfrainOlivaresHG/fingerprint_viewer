#!/usr/bin/env python 
import sys
sys.dont_write_bytecode = True
from flask_script import Manager
from fingerprint_viewer.app import app


manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load

if __name__ == "__main__":
    manager.run()
