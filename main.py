#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import redirect
from flask import url_for
from flask import Response
from flask import session

import logging
import os

from OTAMaker import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/makePlist', methods=['POST'])
def generate_plist():
    url = request.form['app-url']
    bundle_id = request.form['app-bundle-id']
    app_version = request.form['app-version']
    app_name = request.form['app-name']

    plist = make_plist(url, bundle_id, app_version, app_name)
    redirect_path = app_name+".plist"
    session['plist'] = plist
    return redirect(url_for('return_make_plist', filename=redirect_path))


@app.route('/makePlist/<filename>')
def return_make_plist(filename):
    plist = session['plist']
    return Response(plist, mimetype="application/x-plist")


@app.route('/downloadPage')
def download_page():
    return render_template('download.html')

#secret key for using session
app.secret_key = os.urandom(24)
