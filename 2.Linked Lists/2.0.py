#!/usr/bin/env python

import sys

#Linked List

class Node:

	def __init__(self, data, nextnode):
		self.data = data
		self.next = nextnode

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def append_tail(self,nextnode):
		node = self
		while(node.next != None):
			node = node.next
		node.next = nextnode 

def printNode(node):

	while(node != None):
		print node.data
		node = node.next

def createList(numlist):

	result = Node(numlist[0], None)

	for i in range(1,len(numlist)):
		result.append_tail(Node(numlist[i], None))

	return result;

def deleteNode(node, n):

	#Keep track of head of linked list
	head = node

	if(node.data == n):
		node = node.next
		return node

	while(node.next != None):
		if(node.next.data == n):
			node.next = node.next.next
			return head
		node = node.next

	return head

node = Node(5,None)
printNode(node)
linkedlist = createList([1,2,3])
printNode(linkedlist)
newlist = deleteNode(linkedlist, 3)
printNode(newlist)