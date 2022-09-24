from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

print(q.queue[0])

while not q.empty():
    next_item = q.get()
    print(next_item)