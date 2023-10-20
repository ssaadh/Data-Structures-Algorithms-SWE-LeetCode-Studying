
# helper linked list class
class Node:
	def __init__(self, item):
		self.item = item
		self.next = None

class Queue:
	# creates an empty Queue
	def __init__(self):
		self.front = None
		self.end = None

	# adds an item to the queue
	def enqueue(self, item):
		old_end = self.end
		self.end = Node(item)
		self.end.next = None
		if self.is_empty():
			self.front = self.end
		else:
			old_end.next = self.end


	# removes and returns the least recently added item 
	def dequeue(self):
		assert not self.is_empty()
		item = self.front.item
		self.front = self.front.next
		if self.is_empty():
			self.end = None
		return item

	def is_empty(self):
		return self.front == None

if __name__ == "__main__":
	queue = Queue()
	for i in range(0, 5):
		queue.enqueue(i)

	while queue.is_empty() == False:
		print(queue.dequeue())  
	# (0)
	# (1)
	# (2)
	# (3)
	# (4)
