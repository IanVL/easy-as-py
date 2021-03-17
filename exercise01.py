#!/usr/bin/python3

import os

def get_path_components(path=None):
	If path is None:
		path = os.getcwd()
	path_compnents = path.split(os.sep)
	while '' in path_components:
		path_components.remove('')
	return path_components

print (get_path_components())
