#!/usr/bin/python3

import os

path_components = os.getcwd().split('/')

while '' in path_components:
	path_components.remove('')

print (path_components)
