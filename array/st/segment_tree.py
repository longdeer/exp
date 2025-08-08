

# LC3479
class MaxSegmentTree:
	def build(self, node :int, l :int, r :int, arr :List[int]):

		if l == r : self.st[node] = arr[l]
		else:

			m = l + (r -l) //2
			f = node <<1

			self.build(f, l,m, arr)
			self.build(f +1, m +1,r, arr)

			self.st[node] = max(self.st[f],self.st[f+1])

	def update(self, node :int, l :int, r :int, target :int):

		if	l == r:
			if	target <= self.st[node]:
				self.st[node] = 0
				return True
		else:

			m = l + (r -l) //2
			f = node <<1

			if	target <= self.st[f] and self.update(f, l,m, target):

				self.st[node] = max(self.st[f],self.st[f+1])
				return True

			if	target <= self.st[f+1] and self.update(f+1, m +1,r, target):

				self.st[node] = max(self.st[f],self.st[f+1])
				return True

			return False

