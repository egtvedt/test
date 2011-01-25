def square(width, height):
	height -= 2
	width -= 2
	if height < 1:
		height = 1
	if width < 1:
		width = 1

	middle = "*%s*\n" % (" " * width)
	edge   = "*%s*\n" % ("*" * width)

	return edge + middle * height + edge

if __name__ == "__main__":
	print square(10,5)

