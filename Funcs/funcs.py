


"""
Recursive Function:
recursive functions call themselves. To understand them, try copy-pasting 
the entire function each time you see it call itself. 

"""
def recursiveFunc(y):
	"""
	this function will increment a given number then call itself, passing that same number. After
	the called function is done, it will print y. This results in it printing 
	he numbers in reverse order, because the innermost iteration finishes first
	before execution returns to upper iterations. Illustration:

	r = the addition function (y +=1 )
	p = the print part of the funtion (print(y, end=' '))
	y = the var (starting at 0)


	r0 -> r1 -> r2 -> r3 -> p3(4) -> p2(3) -> p(2) -> p0(1)
	y=1	  y=2	y=3	  y=4  
	"""
	y += 1
	if y < 9:
		recursiveFunc(y)
	print(y, end=' ')

def fibonacci(limit=15):
	"""
	Non-recursive fibonacci function
	"""
	a = 1
	b = 1
	for _ in range(limit):
		print(b)
		c = a 
		a += b
		b = c

def recursiveFib(a, b, lim=15):
	if lim:
		c = a 
		a += b
		b = c
		print(b)
		recursiveFib(a, b, lim=lim-1)
		
