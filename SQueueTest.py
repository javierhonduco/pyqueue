import unittest
import random
from SQueue import Queue
queue = Queue()

class Enqueue(unittest.TestCase):
	""" TODO: Decouple test, generate them automatically, test settings. """
	def runTest(self):
                
		assert queue.isEmpty()
		assert queue.size() == 0
		assert queue.toList() == []
		queue.enqueue(0)
		assert queue.first() == 0
		assert queue.last() == 0
		assert queue.toList() == [0]
		queue.enqueue(2)
		assert queue.toList() == [0, 2]
		queue.enqueue(5)
		assert queue.toList() == [0, 2, 5]
		assert queue.first() == 0
		assert queue.last() == 5
		assert queue.dequeue() == 0
		assert queue.toList() == [2, 5]
		assert not queue.isEmpty()
		assert queue.dequeue() == 2
		assert queue.toList() == [5]
		assert queue.dequeue() == 5
		assert queue.isEmpty()
                for a in xrange(5000):
                        queue.enqueue(random.uniform(0, 999999)
         
                 
		assert queue.size() != 0



if __name__ == '__main__':

    unittest.main()   
