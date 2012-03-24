"""
Copyright 2010 Erik Soma <stillusingirc@gmail.com>

This file is part of Derpy Delivery.

Derpy Delivery is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Derpy Delivery is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Derpy Delivery. If not, see <http://www.gnu.org/licenses/>.
"""

import os

root_path = os.path.abspath(os.path.dirname(os.path.relpath(__file__)))

res_path = {
	'img':'img',
	'snd':'snd',
	'font':'font',
	'lvl':'levels'
}

#Convert short paths to full paths
for k, v in res_path.iteritems():
	res_path[k] = os.path.join(root_path, v)
	print "Resource", k, "path:", res_path[k]

window = None
clock = None
imgH = None
objH = None
keyH = None
rmH = None
lvlH = None
space = None
sndH = None
levels = None

#keybindings
leftButton = None
rightButton = None
upButton = None
downButton = None
menuButton = None
startButton = None
oneButton = None
twoButton = None
