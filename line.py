def line(n):
	"""
	Return a string that contains n "*" elements.
	"""
	if n < 0:
		raise Exception("a line can not be shorter than 0")
	return "*" * n

if __name__ == "__main__":
	print line(10)
