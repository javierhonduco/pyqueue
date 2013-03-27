from SNode import Node

class Queue:
	
	def __init__(self):
		self.front 	= None
		self.tail 	= None
		self.settings = {
			"MIX_TYPES" : False,
			"MAX_SIZE"  : None,
 		}
 		self.type 	= -1

	def enqueue(self, element = None):
		if self.settings["MAX_SIZE"] is not None:
			if self.size() < self.settings["MAX_SIZE"]:
				raise Exception("Queue overflow!")
		if self.settings["MIX_TYPES"]:
			if self.type is -1:
				self.type = type(element)
			if type(element) is not self.type:	
				raise Exception("Mixing data types is not allowed")
		new = Node(element)
		if self.tail is None:
			self.front = new
		else:
			self.tail.next = new
		self.tail = new

	def dequeue(self):
		if self.front is None:
			return None
		else:
			element = self.front.element
			self.front = self.front.next
			if self.front is None:
				self.tail = None
		return element

	def isEmpty(self):
		return self.front is None

	def first(self):
		return self.front.element

	def last(self):
		return self.tail.element

	def size(self):
		size = 0
		current = self.front
		while current is not None:
			size += 1
			current = current.next
		return size	

	def toList(self):
		result = []
		current = self.front
		while current is not None:
			result.append(current.element)
			current = current.next
		return result

	def void(self):
		self.tail = None
		self.front = None

	def toString(self):
		result = ""
		current = self.front
		while current is not None:
			result += str(current.element) + ", "
			current = current.next
		return result
