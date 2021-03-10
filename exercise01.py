#!/usr/bin/python3

import os

def get_path_components():
	path_components = os.getcwd().split('/')
	while '' in path_components:
		path_components.remove('')
	return path_components

print (get_path_components())
