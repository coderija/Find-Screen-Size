def ScreenSize(width, ratio):
	#turning ration into a list of two numbers
	r = ratio.split(":")

	#calculate the height 
	height = (width/int(r[0]))*int(r[1])

	#display the string
	return '{}x{}'.format(width, int(height))

print(ScreenSize(1200,'4:3')) 