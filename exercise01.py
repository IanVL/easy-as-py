#!/usr/bin/python3

import os

def get_path_components(path=None):
	'''
	Return the components of a given path or, if not given, the current
	working directory.
	'''
	If path is None:
		path = os.getcwd()
	path_compnents = path.split(os.sep)
	while '' in path_components:
		path_components.remove('')
	return path_components

def (get_path_depth):
	'''
	Return the number of path components in a given path.
	'''
	return len(get_path_components(path))
