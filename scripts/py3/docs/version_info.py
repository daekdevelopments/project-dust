#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2018 The Dust Project
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

version = '0.0.1'
build = 'D-001A'
compiled = '26/11/2018 8:16 PM EST'
channel = 'Alpha/Canary'

print('Project Dust')
print('303541')
print('Version: ' + version)
print('Build: ' + build)
print('Compiled: ' + compiled)
print('Channel: ' + channel)
print('Created By The Dust Project And cmDev Team')

import subprocess as sp
sp.call('pause',shell=True)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
