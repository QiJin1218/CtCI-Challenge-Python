#!/usr/bin/env python

import sys

#Stack

class Stack:

	def __init__(self):
		self.items = []

	def pop(self):
		if(len(self.items)==0):
			print "Warning, empty stack"
			return
		return self.items.pop()
		#or
		# l = len(self.items)
		# item = self.items[l-1]
		# del self.items[l-1]
		# return item

	def push(self, item):
		return self.items.append(item)

	def peek(self):
		if self == None:
			print "Empty stack"
			return
		else:
			return self.items[0]

	def isEmpty(self):
		return len(self.items) == 0

def printStack(stack):

	while(len(stack.items)>0):
		print stack.pop()

def createStack(numlist):

	result = Stack()

	for i in range(len(numlist)):
		result.push(numlist[i])

	return result;

# stack = Stack()
# print stack.isEmpty()
# newStack = createStack([1,2,3])
# printStack(newStack)

class Queue:

	def __init__(self):
		self.items = []

	def remove(self):
		item = self.items[0]
		del self.items[0]
		return item

	def peek(self):
		if(len(self.items)==0):
			print "Empty queue"
			return
		else:
			return self.items[0]

	def additem(self, item):
		self.items.append(item)

	def isEmpty(self):
		return len(self.items) == 0

def printQueue(queue):

	while(len(queue.items)>0):
		print queue.remove()

	return

def createQueue(nlist):

	q = Queue()

	for i in range(len(nlist)):
		q.additem(nlist[i])

	return q

# queue = Queue()
# print queue.isEmpty()
# newqueue = createQueue([4,5,6])
# printQueue(newqueue)