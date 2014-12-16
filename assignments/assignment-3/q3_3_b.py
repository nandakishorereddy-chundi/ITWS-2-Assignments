class WordIterator(object):
	"""Iterates the words of a string"""
	def __init__(self, string):
		self.string = list(string)
		self.start_index = 0
		self.length = len(string)

	def __iter__(self):
		return self
	
	def next(self):
		tmp_word = []
		if self.start_index == self.length :
			raise StopIteration
		for i in xrange(self.start_index, self.length):
			if self.string[i] != ' ':
				tmp_word.append(self.string[i])
			else:
				self.start_index = i + 1
				break
		if i == self.length -1 :
			self.start_index = self.length 
		return ''.join(tmp_word)