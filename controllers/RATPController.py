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
from flask import render_template

from ratp_skill.api import *


@ratp.route('/' , methods=['GET','POST'])
@login_required
def index():
    return render_template('ratp/index.html')

@ratp.route('/config' , methods=['GET','POST'])
@login_required
def config():
    return render_template('ratp/config.html')

@ratp.route('/widget')
@login_required
def widget():
    return render_template('ratp/widget.html')
