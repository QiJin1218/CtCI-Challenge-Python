#!/usr/bin/env python

#1.3

def urlify(s):

	result = ""

	for i in range(len(s)):
		if(s[i] == " "):
			result += '%20'
		else:
			result += s[i]

	return result

s = raw_input("Please enter a string: ")
print urlify(s)