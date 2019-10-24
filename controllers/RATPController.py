# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
"""

from ratp_skill.index import ratp
from flask_login import login_required
from onyxbabel import gettext
from flask import render_template, request, redirect, url_for, flash
from onyx.api.assets import Json
from onyx.api.exceptions import *

from ratp_skill.api import *

json = Json()
ratp_api = Ratp()

@ratp.route('/config' , methods=['GET','POST'])
@login_required
def config():
    return render_template('ratp/config.html')

@ratp.route('/')
def index():
    return render_template('ratp/index.html')

#RER
@ratp.route('/rer', methods=['GET', 'POST'])
def rers():
    if request.method == 'GET':
        return render_template('ratp/ratp/rer/index.html')
    elif request.method == 'POST':
        return redirect('transport/rer/' + request.form['rerline'])

@ratp.route('/rer/<string:name>', methods=['GET', 'POST'])
def rer(name):
    if request.method == 'GET':
        try:
            return render_template('ratp/ratp/rer/'+name+'.html')
        except TransportException:
            return render_template('ratp/ratp/rer/index.html')
    elif request.method == 'POST':
        ratp_api.line = name
        ratp_api.station = request.form['rerstation']
        ratp_api.direction = request.form['rerdirection']
        json.url = ratp_api.get_rer_schedule()
        result = json.decode_url()
        try:
            return render_template('ratp/ratp/rer/result.html', result=result)
        except TransportException:
            flash(gettext('An error has occured !') , 'error')
            return redirect(url_for('ratp.index'))


#METRO
@ratp.route('/metro', methods=['GET', 'POST'])
def metros():
    if request.method == 'GET':
        return render_template('ratp/ratp/metro/index.html')
    elif request.method == 'POST':
        return redirect(url_for('ratp.metro', name=request.form['metroline']))



@ratp.route('/metro/<string:name>', methods=['GET', 'POST'])
def metro(name):
    if request.method == 'GET':
        try:
            return render_template('ratp/ratp/metro/' + name + '.html')
        except TransportException:
            return render_template('ratp/ratp/metro/index.html')
    elif request.method == 'POST':
        ratp_api.line = name
        ratp_api.station = request.form['metrostation']
        ratp_api.direction = request.form['metrodirection']

        json.url = ratp_api.get_metro_schedule()
        result = json.decode_url()
        try:
            return render_template('ratp/ratp/metro/result.html', result=result)
        except TransportException:
            flash(gettext('An error has occured !') , 'error')
            return redirect(url_for('ratp.index'))