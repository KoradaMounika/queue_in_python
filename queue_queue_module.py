#queue impelementation using queue module
import queue
l=queue.Queue(maxsize=5)
l.put(10)
l.put(20)
print(l)
print(type(l))
print(l.get())
print(l.get())
