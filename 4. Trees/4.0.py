#!/usr/bin/env python

import sys

#Binary Tree

class Tree:

	def __init__(self,r):
		self.root = r
		self.left = None
		self.right = None

	#Add a value to a tree
	def addtoTree(self,v):

		t = self.root 

		if(t is None):
			self.root = v
		else:
			if(t > v):
				if(self.left is None):
					self.left = Tree(v)
				else:
					self.left.addtoTree(v)
			else:
				if(self.right is None):
					self.right = Tree(v)
				else:
					self.right.addtoTree(v)

	#Prints out nodes of trees in-order trabersal
	def showTree(self):

		t = self.root

		if(t is None):
			return ""
		else:
			if(self.left is not None):
				self.left.showTree()
			print t
			if(self.right is not None):
				self.right.showTree()

def listtoTree(l):

	t = Tree(l[0])

	for i in l[1:]:
		t.addtoTree(i)

	return t

l = [1,2,5,2,7,3,9,1]
tree = listtoTree(l)
tree.showTree()