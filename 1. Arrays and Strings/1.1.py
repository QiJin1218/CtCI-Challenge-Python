#!/usr/bin/env python

import sys

#1.1
def uniquestr(s):

	hashtable = {};
	for i in range(len(s)):
		if s[i] in hashtable.keys():
			return "F";
		else:
			hashtable[s[i]] = 1;

	return "T";

inputstr = raw_input("Enter a string: ");
print uniquestr(inputstr);