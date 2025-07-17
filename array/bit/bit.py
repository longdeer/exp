

class BIT:
	def __init__(self, size :int):

		self.size = size
		self._inner_ = [ 0 ] *(self.size +1)

	def update(self, i :int):

		j = i +1

		while j <self.size:

			self._inner_[j] += 1
			j += j& -j

	def query(self, i :int) -> int :

		j = i +1
		s = 0

		while 0 <j:

			s += self._inner_[j]
			j -= j& -j

		return s

