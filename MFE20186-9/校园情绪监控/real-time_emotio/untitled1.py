#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:56:29 2018

@author: admin
"""

import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print json