class Video:
	def __init__(self, title, genre, length):
		self.__title = title
		self.__genre = genre
		self.__length = length

	def __str__(self):
		return "Title: {}, Genre: {}, Length: {}".format(self.__title, self.__genre, self.__length)