import	os
import	sys
from	collections	import deque








def make_file(path :str):
	with open(path, "w") as f : f.write("\n\n\tthis is the place for advertisement\n\n")


FLOOD_COUNTER = int(sys.argv[1])	# root doesn't count
flood = deque([( os.getcwd(),1 )])








while flood and 0 <FLOOD_COUNTER:


	for _ in range(len(flood)):
		directory,q = flood.pop()


		for i in range(q):
			current = os.path.join(directory, str(i))


			if	i &1 : make_file(current)
			else:
				os.mkdir(current)
				flood.appendleft(( current,q +1 ))


			FLOOD_COUNTER -= 1
			if	not FLOOD_COUNTER : exit()







