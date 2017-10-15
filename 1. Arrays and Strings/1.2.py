#!/usr/bin/env python

import sys

#1.2
def permutation(s1, s2):

	#Check length
	if (not samelen(s1,s2)):
		return False;

	hashs1 = createhash(s1);
	for i in range(len(s2)):
		if s2[i] not in hashs1.keys():
			return False;

	return True;

def samelen(s1, s2):

	len1 = len(s1);
	len2 = len(s2);

	return (len1 == len2);

def createhash(s):

	result = {};

	for i in range(len(s)):
		result[s[i]] = 1;

	return result;

#Implementation 2: Sort both strings
def permutation2(s1, s2):

	ss1 = sorted(s1);
	ss2 = sorted(s2);

	return (ss1==ss2);

str1 = raw_input("Enter a string: ");
str2 = raw_input("Enter another string: ");
result = (permutation(str1, str2) and permutation(str2, str1));
print "Method 1:\n" + str(result);
print "Method 2:\n" + str(permutation2(str1,str2));

